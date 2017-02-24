__author__ = "shikun"
import db_base
from flask import  session, redirect,url_for, Flask,render_template, send_from_directory
app = Flask(__name__)
# def login_required(func):
#     with app.test_request_context():
#         if session.get('uid') == None:
#             return redirect(url_for('admin.login' ))
check_db = None
def checkDB():
    global check_db
    if check_db == None:
        check_db = db_base.MySQLet(host="127.0.0.1", user="root", password="", charset="utf8", database="api", port=3306)
    return check_db


