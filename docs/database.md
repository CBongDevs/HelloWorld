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

## Initialisation

First, create a new database:

    % createdb financeapi

Then, start a python session (remember to use the virtualenv environment!):

    (.venv) % ipython

Finally, use `flask_sqlalchemy` to initialise it with our tables:

    In [1]: from financeapi import db
    In [2]: db.create_all()

