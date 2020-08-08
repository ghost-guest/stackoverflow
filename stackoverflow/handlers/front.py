from flask import Blueprint, redirect, render_template, jsonify, request, url_for
from ..models import db, User
from flask_login import login_user, current_user, logout_user, login_required


front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html', title='Stack Overflow 首页', tem_str='shiyanlou')

#注册
@front.route('/signup', methods=['POST'])
def signup():
    user = User.query.filter((User.name==request.form['name'])|(User.email==request.form['email'])).first()
    if user:
        return jsonify(status='error', info='已存在该用户')
    user = User(name=request.form['name'], email=request.form['email'],
                password=request.form['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(status='success', info='创建成功')

#登录
@front.route('/login', methods=['POST'])
def login():
    print('前段的请求{}'.format(request.form))
    print('请求中的用户名：{}'.format(request.form['name']))
    user = User.query.filter_by(name=request.form['name']).first()
    print('用户名：{}'.format(user.name))
    if user:
        if user.check_password(request.form['password']):
            print('222222222222222222222222222')
            login_user(user)
            return redirect(url_for('.index'))
        return jsonify(status='error', info='密码错误')
    return jsonify(status='error', info='用户不存在')

#退出登录
@front.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))