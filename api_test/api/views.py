__author__ = "shikun"
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash,jsonify, Blueprint
import db_base, const
from api_test.utilities import *

mysqlet = db_base.MySQLet(host="127.0.0.1", user="root", password="", charset="utf8", database="api", port=3306)
api = Blueprint('api', __name__, template_folder='templates')

@api.route("/list/<id>", methods=['GET'])
def list(id):
    apis = (mysqlet.findKeySql(const.FIND_ALL_BY_ATTR, table="api_info", criteria= {"where": "m_id=" + id}, whole=True))
    id = id
    return render_template("list.html", apis=apis, id=id)

@api.route("/add_api_h")
def add_api_h():
    return render_template('add_api.html')
@api.route('/add_api', methods=['POST'])
def add_api():
    mysqlet.findKeySql(const.INSERT, table="api_info", data={"title":  request.form['title'], "url":  request.form['url'], "param":  request.form['param'],
                                                             "method": request.form['m_method'], "hope_result": request.form['hope_result'],"result": 0,
                                                             "m_id": request.form["mondule_id"]})
    return redirect(url_for('moudle.mondule_info', id=request.form["mondule_id"]))

@api.route("/del_api", methods=["POST"])
def del_api():
    if mysqlet.findKeySql(const.DELETE_BY_ATTR, table="api_info", params={"id": request.form["id"]}):
        return jsonify({'msg': 1})
    else:
        return jsonify({'msg': 0})
