# -- 알아볼 부분
# flask.redirect() - https://github.com/pallets/flask/blob/master/flask/__init__.py#L18
# werkzeug.utils.redirect() - https://github.com/pallets/werkzeug/blob/master/werkzeug/utils.py#L344
# flask.helpers.url_for() - https://github.com/pallets/flask/blob/master/flask/helpers.py#L201

from flask import Flask
from flask import redirect
# = from werkzeug.utils import redirect
from flask import url_for

app = Flask(__name__)


# /index와 /test가 있다고 치자
# 특정 조건에 따라 사용자의 위치를 이동시키는 경우가 생긴다
# ex) index로 접근했을 때 사용자가 로그인되어 있지 않은 경우 signup으로 이동

# redirect 함수를 이용하면 된다. 매개변수는 uri를 넣자
@app.route('/index')
def index():
    return redirect('/test')


@app.route('/test')
def test():
    return 'here is test'


# 만약 함수명을 통해 uri를 얻어내고 싶다면, url_for 함수를  쓰자
@app.route('/index2')
def index2():
    return redirect(url_for('test'))

app.run(debug=True)
