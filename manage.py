from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

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

    # flask_session的配置信息
    SESSION_TYPE = 'redis' # 指定session 保存到redis 中
    SESSION_USE_SIGNER = True # 让　cookie 中的session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT) #使用redis的实例
    PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期


app.config.from_object(Config)
db = SQLAlchemy(app)
Session(app)

# 创建redis储存对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)


@app.route("/")
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
