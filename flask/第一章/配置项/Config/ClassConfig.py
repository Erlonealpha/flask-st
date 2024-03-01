# 定义配置类
class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = 'your_secret_key'
