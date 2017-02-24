# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash,jsonify

import db_base, const

# configuration
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

app = Flask(__name__)
# app.config.from_object(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['SECRET_KEY'] = '123456'
mysqlet = db_base.MySQLet(host="127.0.0.1", user="root", password="", charset="utf8", database="api", port=3306)
@app.route('/')
def index():
    if session.get('logged_in') != None:
        moudles = mysqlet.findKeySql(const.FIND_BY_ALL, sql="select * from moudle" )
        print(moudles)
        return render_template('index.html', moudles=moudles)
    else:
        return render_template('login.html', error="没有登录")
@app.route('/mondule_info/<id>')
def mondule_info(id):
    apis = (mysqlet.findKeySql(const.FIND_ALL_BY_ATTR, table="api_info", criteria= {"where": "m_id=" + id}, whole=True))
    print(apis)
    id = id
    return render_template('mondule_info.html', apis=apis, id=id)

@app.route('/add_moudle_h')
def add_moudle_h():
    return render_template('add_moudle.html')

@app.route('/add_moudle', methods=['POST'])
def add_moudle():
    if not session.get('logged_in'):
        abort(401)
    flash('新增模块中')
    mysqlet.findKeySql(const.INSERT, table="moudle", data={"title": request.form['title'], "host": request.form['host'],
                        "port":request.form.get('port'), "header": request.form.get('header')})
    flash('新增模块成功')
    return redirect(url_for('index'))


@app.route("/add_api_h")
def add_api_h():
    return render_template('add_api.html')
@app.route('/add_api', methods=['POST'])
def add_api():
    if not session.get('logged_in'):
        abort(401)
    flash('新增api中')
    mysqlet.findKeySql(const.INSERT, table="api_info", data={"title":  request.form['title'], "url":  request.form['url'], "param":  request.form['param'],
                                                             "method": request.form['m_method'], "hope_result": request.form['hope_result'],"result": 0,
                                                             "m_id": request.form["mondule_id"]})
    flash('新增api成功')
    return redirect(url_for('mondule_info', id=request.form["mondule_id"]))

@app.route("/del_api", methods=["POST"])
def del_api():
    if mysqlet.findKeySql(const.DELETE_BY_ATTR, table="api_info", params={"id": request.form["id"]}):
        return jsonify({'msg': 1})
    else:
        return jsonify({'msg': 0})

@app.route('/login_h')
def login_h():
    return render_template('login.html', error="没有登录")
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if mysqlet.findKeySql(const.EXIST, table="user", params={"username": request.form['username'], "pwd": request.form['password']}, join='AND'):
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
        else:
            error = '用户名或密码错误'
            return render_template('login.html', error=error)
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('login.html', error="您已经退出登录了")


if __name__ == '__main__':
    app.run(debug=True)