import json

from flask import Flask, flash, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hogworts:hogworts@47.110.37.80:49158/test_platform?charset=utf8mb4'
db = SQLAlchemy(app)

'''
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
'''


class TestUser(db.Model):
    username = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(1000), unique=False, nullable=True)
    def __repr__(self):
        return '<TestCase %r>' % self.username


"""
https://flask-restful.readthedocs.io/en/latest/quickstart.html#

"""
def read_res(file):
    with open(file, encoding='utf-8') as f:
        datas = json.load(f)
        f.close()
    return datas

class SignUpServices(Resource):
    # testcases=[]
    def get(self):
        education = request.args.get('education', None)
        if education:
            datas = read_res("test.json")
            return datas,200,[("Access-Control-Allow-Credentials","true")]

            # testcase = TestUser.query.filter_by(username=username).first()
            # return {'code': "0000", 'message': str(testcase), 'success': True}
        else:
            # return 响应体, 状态码, 响应头
            datas = read_res("res.json")
            app.logger.info(datas)
            return datas,200,[("Access-Control-Allow-Credentials","true")]
            # testcases = TestUser.query.all()
            # return {'code': "0000", 'message': [str(testcase) for testcase in testcases], 'success': True}
            #Access-Control-Allow-Credentials

    def post(self):
        username = request.json.get('username'),

        testcase = TestUser(
            username=request.json.get("username"),
            email=request.json.get('email'),
            password=json.dumps(request.json.get("password"))
        )

        query_testcase = TestUser.query.filter_by(username=username).first()
        if query_testcase:
            return {'code': "0001", 'message': f'{username} is existed', 'success': False}
        else:
            db.session.add(testcase)
            db.session.commit()
            testcase = TestUser.query.filter_by(username=username).first()
            return {'code': "0000", 'message': str(testcase), 'success': True}

    def put(self):
        username = request.args.get('username', None)
        testcase = TestUser(
            username=request.json.get("username"),
            email=request.json.get('email'),
            password=json.dumps(request.json.get("password"))
        )
        if username:
            # name=name 中间不可以加空格
            query_testcase = TestUser.query.filter_by(username=username).first()
            if query_testcase:
                return {'code': "0001", 'message': f'{username} is existed', 'success': False}
            else:
                db.session.add(testcase)
                db.session.commit()
                return {'code': "0000", 'message': 'completed', 'success': True}
        else:
            return {'code': "0002", 'message': f'{username} is not found,please check', 'success': False}

    def delete(self):
        name = request.json['username']
        testcase = TestUser.query.filter_by(username=name).first()
        if testcase:
            db.session.delete(testcase)
            db.session.commit()
            return {'code': "0000", 'message': 'completed', 'success': True}
        else:
            return {'code': "0001", 'message': f'{name} is not found', 'success': False}


class SignInServices(Resource):
    # testcases=[]
    def post(self):

        username = request.json.get('username'),

        testcase = TestUser(
            username=request.json.get("username"),
            email=request.json.get('email'),
            password=json.dumps(request.json.get("password"))
        )

        query_testcase = TestUser.query.filter_by(username=username).first()
        if query_testcase:
            return {'code': "0001", 'message': f'{username} is existed', 'success': False}
        else:
            db.session.add(testcase)
            db.session.commit()
            testcase = TestUser.query.filter_by(username=username).first()
            return {'code': "0000", 'message': str(testcase), 'success': True}


api.add_resource(SignUpServices, '/cabinx/pcapi/table/data')
api.add_resource(SignInServices, '/user/login')


if __name__ == '__main__':
    app.run(debug=True,port=80)
