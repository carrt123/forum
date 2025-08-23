from flask import Blueprint, render_template, request, current_app, url_for, redirect, flash, session
from exts import mail, cache, db
import random
from utils.restful import response
from forms.user import RegisterForm, LoginForm
from models.user import UserModel

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("front/register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            for message in form.messages:
                flash(message)
            return redirect(url_for('user.register'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("front/login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = UserModel.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                if remember:
                    session.permanent = True
                return redirect('/')
            else:
                flash("邮箱或密码错误!")
                return redirect(url_for("user.login"))
        else:
            for message in form.messages:
                flash(message)
            return render_template("front/login.html")


@bp.route("/mail/captcha")
def mail_captcha():
    email = "18770055812@163.com"
    # email = request.args.get("mail")
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    captcha = "".join(random.sample(digits, 4))
    subject = "【python论坛】验证码"
    body = f"【python论坛】您的注册验证码是: {captcha}, 请勿告诉他人!"
    # message = Message(subject="python论坛验证码", recipients=[email], body=body)
    try:
        # mail.send(message)
        current_app.celery.send_task("send_mail", (email, subject, body))
        cache.set(email, captcha, timeout=100)
        return response.success("email has been send!")
    except Exception as e:
        return f"failed to send email: {e}"
