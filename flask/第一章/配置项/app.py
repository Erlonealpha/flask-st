import json

from flask import Flask

# class Config():
#     ENV = 'development'
#     DEBUG = True
#     TESTING = False

app = Flask(__name__)
# app.config.from_object(Config)

# app.config.from_file("Config/config.json",json.load)

# app.config.from_pyfile("Config/config.py")

# app.config.update(
#     ENV = "development",
#     DEBUG = True,
#     TESTING = False
# )

# app.config['ENV'] = 'development'
# # 例如，开启调试模式
# app.config['DEBUG'] = True
# # 设置测试标志
# app.config['TESTING'] = False

@app.route('/')
def index():
    # 获取当前的运行环境（默认是 production，除非通过FLASK_ENV环境变量设置）
    env = app.config['ENV']
    # 获取当前的调试状态
    debug = app.config['DEBUG']
    # 获取当前的测试状态
    testing = app.config['TESTING']

    # 使用<br>来在网页上实现换行
    return f"当前运行环境：{env}<br>调试模式：{debug}<br>测试模式：{testing}"

if __name__ == "__main__":
    app.run()
