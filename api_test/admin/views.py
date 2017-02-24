__author__ = "shikun"
import os
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash,jsonify, Blueprint
import db_base, const
from api_test.utilities import *
mysqlet = db_base.MySQLet(host="127.0.0.1", user="root", password="", charset="utf8", database="api", port=3306)
# api = Blueprint( 'site',__name__,template_folder='templates',static_folder='static')
admin = Blueprint('admin', __name__, template_folder='templates')
@admin.route('/login_h', methods=['GET'])
def login_h():
    return render_template('login.html', error="没有登录")
@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if mysqlet.findKeySql(const.EXIST, table="user", params={"username": request.form['username'], "pwd": request.form['password']}, join='AND'):
            session['uid'] = request.form['username']
            # session['ts'] = time.time()
            flash('You were logged in')
            return redirect(url_for('moudle.index'))
        else:
            error = '用户名或密码错误'
            return redirect(url_for('admin.login_h'))



@admin.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('login.html', error="您已经退出登录了")