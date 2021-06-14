import redis
from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect

from config import Config

app = Flask(__name__)

app.config.from_object(Config)
# 配置数据库
db = SQLAlchemy(app)
# 配置redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护
CSRFProtect(app)
# 设置session保存位置
Session(app)
