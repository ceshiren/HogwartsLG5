import json
import zipfile
from io import BytesIO

from flask import Flask, request, config, make_response, send_from_directory, jsonify, Response,  stream_with_context, send_file
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from downloadlog import download
from basic_api import basic_API
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app, supports_credentials=True)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:songzhaoruizx@127.0.0.1:3306/python?charset=utf8mb4'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:songzhaoruizx@192.168.50.232:3306/python?charset=utf8mb4'
db = SQLAlchemy(app)

# jenkins = Jenkins(
#
#     'http://localhost:8081/',
#     username='john',
#     password='11e79888ce5aec90cfacae0bdfdb673b71'
# )


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(1000), unique=False, nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'steps': self.steps
        }


# 测试用例的管理
class TestCaseService(Resource):
    def get(self):
        name = request.args.get('name', None)
        app.logger.info({'name': name})
        if name:
            testcase = TestCase.query.filter_by(name=name).first()
            return str(testcase)
        else:
            testcases = TestCase.query.all()
            app.logger.info({'testcases': testcases})
            return [testcase.as_dict() for testcase in testcases]

    def post(self):
        testcase = TestCase(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps"))
        )

        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase.query.all()
        return [str(testcase) for testcase in testcases]

    def put(self):
        pass

    def delete(self):
        name = request.json['name']
        testcase = TestCase.query.filter_by(name=name).first()
        db.session.delete(testcase)
        testcases = TestCase.query.all()
        app.logger.info({'testcases': testcases})
        return [str(testcase) for testcase in testcases]



# user表创建
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=True)

    def __repr__(self):
        return '<UserInfo %r>' % self.username

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class UserSignup(Resource):
    def post(self):
        userinfo = UserInfo(
            id=request.json.get("id"),
            username=request.json.get('username'),
            password=request.json.get('password')
        )
        db.session.add(userinfo)
        db.session.commit()


class UserLogIn(Resource):
    def post(self):
        name = request.json.get('username')
        pwd = request.json.get('password')
        app.logger.info({'name': name, 'pwd': pwd})
        if name:
            user = UserInfo.query.filter_by(username=name).first()
            if user == None:
               return 1001
            else:
                print(user.as_dict())
                if pwd == user.as_dict()['password']:
                    print('ok,right person!')
                    return 200
                else:
                    return 1001

"""
# 测试套件，一个条件包含带有顺序的测试用例列表。
# 更复杂的情况是一个套件，可以包含子套件，子套件之间具备串并行关系
# xUnit概念
# pytest dir => [test_1.py::test_a, test_1.py::test_b, test_2.py::test_c]
# suite test_python.py
# suite [test_1.py::test_a, test_1.py::test_b, test_2.py::test_c]
class Suite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    testcases = db.Column(db.String(1000), unique=False, nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'testcases': json.loads(self.testcases)
        }

    def __repr__(self):
        return '<Suite id=%d name=%r >' % (self.id, self.name)


class SuiteService(Resource):
    def get(self):
        id = request.args.get('id', None)
        app.logger.info({'id': id})
        if id:
            suite = Suite.query.filter_by(id=id).first()
            return str(suite)
        else:
            suites = Suite.query.all()
            app.logger.info({'suites': suites})
            return [suite.as_dict() for suite in suites]

    def post(self):
        suite = Suite(
            name=request.json.get('name'),
            testcases=json.dumps(request.json.get("testcases"))
        )

        db.session.add(suite)
        db.session.commit()

        suites = Suite.query.all()
        return [str(suite) for suite in suites]


# 根据套件的id，取到对应的存在的套件，并把套件的数据发送给jenkins进行执行
# class ExecutionService(Resource):
#     def post(self):
#         suite_id = request.json.get('suite_id')
#         suite = Suite.query.filter_by(id=suite_id).first()
#
#         jenkins.jobs['lagou5_testcase'].invoke(
#             build_params={
#                 'suite': json.dumps(suite.as_dict()),
#                 'command': f'echo git clone https://github.com/ceshiren/HogwartsLG5.git .;'
#                            f'echo 安装虚拟环境与依赖'
#                            f'echo pytest {suite.testcases}'
#                            f'echo 回传结果 curl'
#             }
#         )


class Result:
    pass


# jenkins通过curl命令或者全天的客户端工具，把测试结果，主要是junit.xml allure报告上传回来
class ResultService(Resource):
    pass


class Report:
    pass
"""

class NasServe(Resource):
    def post(self):
        uid = request.json.get('uid')
        app.logger.info({'uid': uid})
        ba = basic_API()
        ban_id = uid  # "6002698378254500b9eb66d1"  # 6079336ad0845d2d5d603e2a johnnyR
        # ba.make_normal(ban_id)
        accounts = ba.get_shared_account(ban_id)
        print(accounts)
        ba.make_normal(accounts[2])
        return accounts

class DownloadLog(Resource):
    def post(self):
        time = request.json.get('time')
        loguid = request.json.get('loguid')
        args = [time, loguid]
        app.logger.info({'time': time, 'uid': loguid})
        mes = download(args)
        print(mes)

        response = make_response(send_file(filename_or_fp=mes, mimetype='zip', as_attachment=True, add_etags=False))
        response.headers["Content-Disposition"] = "attachment; filename={};".format(mes)
        return response


        # import os
        # with open(mes, 'r') as f:
        #     data = f.readlines()
        # # os.remove(os.path.join(path, zipname))
        # return Response(data, headers={
        #     'Content-Type': 'application/zip',
        #     'Content-Disposition': 'attachment; filename=%s;' % mes[35:]
        # })

        # return f'下载完成,下载路径为 {mes}'

class SignUpJohnny(Resource):
    def post(self):
        ba = basic_API()
        nas_token = ba.get_nas_token()
        res = ba.sign_up(int(ba.get_user_dispalyname(nas_token))+1, ba.image("./pic.jpeg"))
        return res


api.add_resource(TestCaseService, '/testcase')
# api.add_resource(SuiteService, '/suite')
api.add_resource(NasServe, '/makeNormal')
api.add_resource(UserLogIn, '/signin')
api.add_resource(UserSignup, '/signup')
api.add_resource(DownloadLog, '/downloadLog')
api.add_resource(SignUpJohnny, '/signUpJohnny')
# api.add_resource(ExecutionService, '/execution')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
