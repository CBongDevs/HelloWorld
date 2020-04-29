# Enables the interactive debugger and reloader when calling `flask run`,
# and takes flask out of production mode.
FLASK_ENV=development
# gunicorn uses port 8000 by default, so make flask use it too.
FLASK_RUN_PORT=8000

FLASK_APP=app