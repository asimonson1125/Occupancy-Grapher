from os import environ as env

SQLALCHEMY_DATABASE_URI = env.get(
    'SQLALCHEMY_DATABASE_URI', 'sqlite:///students.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'