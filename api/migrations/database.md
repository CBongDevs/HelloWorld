# Database and Migrations

The template is configured to use a postgres database. The environment variable `DATABASE_URL`
configures the location of the database. The template was tested using Postgres 12.2. The
template includes migrations out of the box.

## Initial Setup

1. Make sure that a local instance of postgres is running.
2. Execute `createdb <database-name>` to create a new database.
3. Configure `DATABASE_URL` to point to the newly created database.
4. Delete the following directory: `api/migrations/versions/`.
5. Delete unneeded models from the directory: `api/models/`.
6. Remove relevant import statements from `api/models/__init__.py`.
7. Commit the changes.

## Migrations

The workflow for making changes to the models is as follows:
1. Create, edit, or delete a model from the directory `api/models`.
2. Added/remove import statements to `api/models/__init__.py`.
3. Run `flask db migrate` to create a new migration.
4. Run `flask db upgrade` to upgrade the local database.
5. Test your changes.
6. Commit the migration located in: `api/migrations/versions`.

Note: import statements are included in the `api/models/__init__.py` to make
the models easier to import. For example, without the imports the `User` a 
class located in the models module would be imported by writing `import api.models.user.User`.

To migrate the production postgres database, execute:

    heroku run flask db upgrade

Make sure to commit the migration scripts created in step 3.

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
