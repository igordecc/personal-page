import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = "POSTGRESQL.CONNECT ME" # TODO: insert postgresql connection
        g.db.row_factory = "POSTGRES ROW FACTORY" # is it necessary? realy?
    return g.db

def close_db(e=None):
    # this is necessary. import db -> db_get.db() -> db.close_db() is gooood
    db = g.pop('db', None)

    if db is not None:
        db.close()