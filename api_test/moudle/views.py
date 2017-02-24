__author__ = "shikun"
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash,jsonify, Blueprint
import db_base, const
from api_test.utilities import *
from api_test import api
mysqlet = db_base.MySQLet(host="127.0.0.1", user="root", password="", charset="utf8", database="api", port=3306)
moudle = Blueprint('moudle', __name__, template_folder='templates')

@moudle.route('/')
def index():
    moudles = mysqlet.findKeySql(const.FIND_BY_ALL, sql="select * from moudle" )
    print(moudles)
    return render_template('index.html', moudles=moudles)

@moudle.route('/add_moudle_h')
def add_moudle_h():
    return render_template('add_moudle.html')

@moudle.route('/mondule_info/<id>')
def mondule_info(id):
    # apis = (mysqlet.findKeySql(const.FIND_ALL_BY_ATTR, table="api_info", criteria= {"where": "m_id=" + id}, whole=True))
    # print(apis)
    # id = id
    # return render_template('mondule_info.html', apis=apis, id=id)
    return redirect(url_for("api.list", id=id))

@moudle.route('/add_moudle', methods=['POST'])
def add_moudle():
    mysqlet.findKeySql(const.INSERT, table="moudle", data={"title": request.form['title'], "host": request.form['host'],
                        "port":request.form.get('port'), "header": request.form.get('header')})
    return redirect(url_for('index'))
