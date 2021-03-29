import json

from flask import Flask, flash, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hogworts:hogworts@47.110.37.80:49158/test_platform?charset=utf8mb4'
db = SQLAlchemy(app)

'''
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
'''


class TestUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(1000), unique=False, nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.name


"""
https://flask-restful.readthedocs.io/en/latest/quickstart.html#

"""


class SignUpServices(Resource):
    # testcases=[]
    def get(self):
        name = request.args.get('name', None)
        if name:
            testcase = TestUser.query.filter_by(name=name).first()
            return {'code': "0000", 'message': str(testcase), 'success': True}
        else:
            testcases = TestUser.query.all()
            return {'code': "0000", 'message': [str(testcase) for testcase in testcases], 'success': True}

    def post(self):
        name = request.json.get('name'),

        testcase = TestUser(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps"))
        )

        query_testcase = TestUser.query.filter_by(name=name).first()
        if query_testcase:
            return {'code': "0001", 'message': f'{name} is existed', 'success': False}
        else:
            db.session.add(testcase)
            db.session.commit()
            testcase = TestUser.query.filter_by(name=name).first()
            return {'code': "0000", 'message': str(testcase), 'success': True}

    def put(self):
        name = request.args.get('name', None)
        testcase = TestUser(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps"))
        )
        if name:
            # name=name 中间不可以加空格
            query_testcase = TestUser.query.filter_by(name=name).first()
            if query_testcase:
                return {'code': "0001", 'message': f'{name} is existed', 'success': False}
            else:
                db.session.add(testcase)
                db.session.commit()
                return {'code': "0000", 'message': 'completed', 'success': True}
        else:
            return {'code': "0002", 'message': f'{name} is not found,please check', 'success': False}

    def delete(self):
        name = request.json['name']
        testcase = TestUser.query.filter_by(name=name).first()
        if testcase:
            db.session.delete(testcase)
            db.session.commit()
            return {'code': "0000", 'message': 'completed', 'success': True}
        else:
            return {'code': "0001", 'message': f'{name} is not found', 'success': False}


class SignInServices(Resource):
    # testcases=[]
    def post(self):

        name = request.json.get('name'),

        testcase = TestUser(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps"))
        )

        query_testcase = TestUser.query.filter_by(name=name).first()
        if query_testcase:
            return {'code': "0001", 'message': f'{name} is existed', 'success': False}
        else:
            db.session.add(testcase)
            db.session.commit()
            testcase = TestUser.query.filter_by(name=name).first()
            return {'code': "0000", 'message': str(testcase), 'success': True}


api.add_resource(SignUpServices, '/user/register')
api.add_resource(SignInServices, '/user/login')


if __name__ == '__main__':
    app.run(debug=True)
