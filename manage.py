from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from config import Config
from info import app, db

# Flask-script
manager = Manager(app)
# 数据库的迁移扩展
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
