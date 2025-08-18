from flask import Blueprint, render_template, request
from flask_mail import Message
from exts import mail
import random

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route("/register")
def register():
    return render_template("register.html")


@bp.route("/mail/captcha")
def mail_captcha():
    # email = request.args.get("mail")
    email = "18770055812@163.com"
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    captcha = "".join(random.sample(digits, 4))
    body = f"【python论坛】您的注册验证码是: {captcha}, 请勿告诉他人!"
    message = Message(subject="python论坛验证码", recipients=[email], body=body)
    try:
        mail.send(message)
        return "邮件发送成功"
    except Exception as e:
        return f"邮件发送失败: {e}"
