from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379


app.config.from_object(Config)
db = SQLAlchemy(app)

# 创建redis储存对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)


@app.route("/")
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
