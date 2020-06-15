#!python

import click
import json
import requests
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from sys import exit, stderr
from os import getenv

HEROKU_API_TOKEN = getenv("HEROKU_API_TOKEN")
if HEROKU_API_TOKEN is None:
    print('HEROKU_API_TOKEN was not provided. Make sure this is set in an environmental variable (or secret on Github)!', file=stderr)
    exit(-1)

headers = {
    'Accept': 'application/vnd.heroku+json; version=3',
    'Authorization': f'Bearer {getenv("HEROKE_APh_TOKEN")}'
}


def builds_api(app_name):
    return f'https://api.heroku.com/apps/{app_name}/builds'


def sources_api(app_name):
    return f'https://api.heroku.com/apps/{app_name}/sources'


def apps_api():
    return f'https://api.heroku.com/apps'


def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[((n // 10) % 10 != 1) *
                                   (n % 10 < 4) * n % 10::4])


@click.group()
def cli():
    pass


@cli.command('list-apps')
def apps():
    data = requests.get(apps_api(), headers=headers).json()
    print(json.dumps(data, indent=4))


@cli.command('list-builds')
@click.option('-a', '--app', required=True)
def list_builds(app):
    print(f'GET {builds_api(app)}')
    response = requests.get(builds_api(app), headers=headers)
    builds = response.json()
    print('id'.ljust(32),
          'status'.ljust(10),
          'created_at'.ljust(20),
          'source_blob.version',
          sep='\t')
    print('-' * 120)
    for build in builds:
        print(build['id'],
              build['status'].ljust(10),
              build['created_at'],
              build['source_blob']['version'],
              sep='\t')


@cli.command('build-output')
@click.option('-n',
              '--nth',
              help='show the nth build output',
              type=int,
              default=1)
@click.option('-a', '--app', required=True)
def build_output(app, nth):
    response = requests.get(builds_api(app), headers=headers)
    builds = response.json()
    builds = sorted(builds, key=lambda a: a['created_at'], reverse=True)
    if len(builds) < nth - 1:
        print(f'could not find the {ordinal(nth-1)} most recent build')
    else:
        output_url_stream = builds[nth]['output_stream_url']
        response = requests.get(output_url_stream, stream=True)
        for chunk in response.iter_content(chunk_size=None):
            print(chunk.decode('utf8'))


def extract_query_params(url_str):
    # url_str contains query parameters that are not interpreted by requests.
    o = urlparse(url_str)
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    return (url, query)


def get_git_revision(base_path):
    git_dir = Path(base_path) / '.git'
    with (git_dir / 'HEAD').open('r') as head:
        ref = head.readline().split(' ')[-1].strip()

    with (git_dir / ref).open('r') as git_hash:
        return git_hash.readline().strip()


def request_source_blob_endpoint(app):
    print('Requesting source blob endpoints...')
    source_blob = requests.post(sources_api(app), headers=headers).json()['source_blob']
    get_url = source_blob['get_url']
    put_url = source_blob['put_url']
    return (get_url, put_url)


def upload_artifact(artifact_file, put_url):
    data = artifact_file.read()
    (url, params) = extract_query_params(put_url)
    print(f'Uploading {artifact_file.name} to heroku...')
    response = requests.request('PUT', url, params=params, data=data)
    print(response)
    if not response.ok:
        print(f'error: {response.text}')
        exit(1)


@cli.command('deploy')
@click.argument('artifact', type=click.File('rb'))
@click.option('-a', '--app', required=True)
def deploy(artifact, app):
    version = get_git_revision('.')
    get_url, put_url = request_source_blob_endpoint(app)
    upload_artifact(artifact, put_url)
    print('Creating new release...')
    print(f'Version sha: {version}')
    msg = {'source_blob': {'url': get_url, 'version': get_git_revision('.')}}
    response = requests.post(builds_api(app), json=msg, headers=headers)
    print(response)
    print(response.text)


if __name__ == '__main__':
    cli()
