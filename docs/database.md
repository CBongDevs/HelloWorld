# Database

The choice of database is actually a tricky one. The database we pick will depend upon the model
and performance requirements. Typical scenarios are relational databases. As such we'll pick 
postgres because of it's popularity.

## Installation

You need to install postgres version 12.2 on your local system.

### macOS

First install postgres provided through homebrew:

    % brew install postgres

Then somehow make sure the postgres server is running. To have postgres started automatically at
right now and at login, execute:

    % brew services start postgresql

To verify postgres is working, execute:

    % psql
    psql (12.2)
    Type "help" for help.

If you see the below output, all is well and you are able to interact with the database.

## Tips and Tricks

- Databases are listed with `\l`. 
- To change database, type `\c <database>`. 
- SQL statements must be terminated using a semicolon.
- To quit, type `\q`.
- Sometimes, the table name must be surrounded with quotes, e.g. `drop table "user"`.

## Initialisation

First, create a new database:

    % createdb financeapi

Then, upgrade your database to the latest schema:

    % python manage.py db upgrade

## Migrations

In general:
1. `python manage.py db init` is ran once to initialise the migrations directory on project creation.
2. You create a new class in the models directory.
3. `python manage.py db migrate` to create a migration script.
4. `python manage.py db upgrade` to upgrade the postgres database.

To migrate the production postgres database, execute:

    heroku run python manage.py db upgrade

Make sure to commit the migration scripts created in step 3.
