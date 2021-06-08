from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager

app = Flask(__name__)
from config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
Session(app)

# 创建redis储存对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
