## 直接配置
def dirct_config(app):
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'

def multi_config(app):
    app.config.update(
        TESTING=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
    )