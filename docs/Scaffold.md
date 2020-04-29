# Scaffold

## First, let's use common vocabulary.

**Javascript Client**: The entire application code runs in a user-agent, besides from a http server 
which servers static files.

**Server App**: The application renders views and uses traditional get and post requests to perform 
methods on a server.

**Web Api**: The application uses traditional http methods but is not concerned with how users 
interact with it.

**Native App**: The application runs on a native platform, such as iOS or Android.

## Javascript Client + Web Api

This project scaffolds a **Web Api** and a **Javascript Client**. Confusingly, the Javascript 
Client is located in `web` and the Web Api is located in `api`.

From here on, **Api** refers to the Web Api, and **Web** refers to the Javascript Client.

**Api** is written in python uses [flask] as the router middlewear and [sqlalchemy] as the database 
connector. Migrations are managed using [flask-migrate]. Python dependencies must be explicitly 
provided in `requirements.txt`. [venv] is used to isolate application dependencies from system
dependencies. This project uses Python 3.8.2. Api by default runs on port 8000. [gunicorn] is used
as the production server.

[flask-migrate]: https://flask-migrate.readthedocs.io/en/latest/
[flask]: https://flask.palletsprojects.com/en/1.1.x/
[sqlalchemy]: https://docs.sqlalchemy.org/en/13/
[venv]: https://docs.python.org/3/library/venv.html
[gunicorn]: https://gunicorn.org

**Web** is a react app written in Typescript. Web is served during development on using Webpack. Any
calls to Api made under `/api` proxied to Api. Web is served by Api in production mode.

## Cloud Provider: Heroku

The git repository is setup to delpoy to Heroku when pushes are made to the master branch. 

## Tools

If you have not already created your virtual environment, do so now by executing:

    $ python3 -m venv .venv
    c:\>c:\Python38\python -m venv c:\path\to\project\.venv

This creates a new virtual environment located under `.venv` subdirectory.

Activate the virtual environment by executing:

    $ source .venv/bin/activate

**Note:** `(.venv)` indicates that the command is being ran in a python virtual environment.

In Visual Studio Code, the command will be automatically executed when a new terminal is opened.
**Note:** the python extension must be loaded. Opening a python file causes the extension to load.
**Note:** there is a small delay between opening the terminal and Visual Studio Code injecting the
command.

Next, install the dependencies:

    (.venv) $ pip install -r api/requirements.txt

Api can be ran in development mode by executing:

    (.venv) $ flask run

Flask automatically reloads Api when changes are made to the source files.

Api may also be ran in production mode by executing:

    (.venv) $ gunicorn app # or
    (.venv) $ FLASK_ENV=production flask run

In Windows CMD, but remember to unset the environment variable:

    (.venv) > set FLASK_ENV=production
    (.venv) > flask run

## Todo

1. Migrations
2. Setup postgres database
3. Linting
4. Tests
5. Setup environment script
6. Check that stuff is convenient to use in the interpreter.
7. Bake in concurrency libraries

## Api Setup

My gut feeling is that there is a disadvantage to using global variables as recommended in the flask tutorials.

A few notes:
1.  Using the recommended initialisation flow restricts the python process from hosting one app. This is a problem if
    we need to run multiple instances of the app in the same process, which is unlikely.
2.  What happens when we need to connect to the database inside of a script? Import the Api and use its models. If
    each version of the api is located in a separate package, then selectively importing the desired version will
    attach it to the app context (and hence db).


## Greenlet

Greenlets lose their call stack. Debugging support is achieved by installing an extension and setting traces. Determining who called the switch is impossible without it. Exceptions thrown by say `gr1.switch()` aren't propagated to `test1` but are instead propagated to `main` (the root greenlet).

Greenlets are useful when you need to control exactly when your code runs.

## Trio

Trio isn't as feature complete as Curio but otherwise stable.

## Flask

Flask by default isn't multi-threaded. Gunicorn apparently can multithread flask, or 

Greenlet, flask, trio, curio, celery.
