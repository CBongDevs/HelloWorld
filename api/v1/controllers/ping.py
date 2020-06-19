from datetime import datetime
from flask import Blueprint

# Demonstrates how to write and register a blueprint.
#
# A blueprint is flask's builtin way of organizing views and code. Conceptually,
# a *controller file* behaves similarly to class in a statically typed language.
# Only a single instance is ever created, called `controller`. Methods in a
# statically typed class correspond to functions declared in the module's scope.
#
# `api.v1.create_app` attaches all of the controllers to the app - every
# controller must be manually added there. The routing is scoped, so for example
# the endpoint `ping` eventually ends up being located at `/api/v1/ping`.

controller = Blueprint('ping', __name__)

def get_current_time():
    return datetime.now()

@controller.route('/ping')
def ping():
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Ping</title>
        </head>
        <body>
            <h1>Ping</h1
            <p>Current Time: {get_current_time()}</p>
        </body>
    </html>
    """
