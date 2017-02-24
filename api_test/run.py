__author__ = "shikun"
from flask import Flask, session, render_template,redirect,url_for
from api_test.admin.views import admin
from api_test.moudle.views import moudle
from api_test.api.views import api
app = Flask(__name__)

@app.route('/')
def index():
    if session.get('uid') == None:
        return redirect(url_for('admin.login_h'))
    return redirect(url_for('moudle.index'))
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(moudle, url_prefix='/moudle')
app.register_blueprint(api, url_prefix='/api')
if __name__=='__main__':
    app.config['SECRET_KEY'] = '123456'
    app.run(debug=True)