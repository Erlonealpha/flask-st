from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.163.com',       # 服务器
    MAIL_PORT=465,                    # 端口
    MAIL_USE_SSL=True,                # SSL开启情况
    MAIL_USERNAME='example@163.com',  # 邮箱
    MAIL_PASSWORD= ' '                # 安全码
)

mail = Mail(app)

@app.route('/send-mail')
def send_mail():
    msg = Message("Hello email from Flask-Mail",
                  sender="example@163.com",               # 发送邮箱
                  recipients=["cxli1991@163.com"])        # 接收邮箱

    msg.body = f"学号：{20030731}\n班级：{'三年二班'}\n姓名：{'周杰伦'}"
    mail.send(msg)
    return "Mail sent!"


if __name__ == "__main__":
    app.run()
