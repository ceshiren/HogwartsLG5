import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou5:hogwarts@stuq.ceshiren.com:23306/lagou5db?charset=utf8mb4'
db = SQLAlchemy(app)

jenkins = Jenkins(
    'http://stuq.ceshiren.com:8020/',
    username='seveniruby',
    password='11d937bfe0f5cdf06fb70074e12dfcac6c'
)
# testcases = []

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(1000), unique=False, nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.name

class TestCaseService(Resource):
    def get(self):
        name=request.args.get('name', None)
        app.logger.info({'name': name})
        if name:
            testcase=TestCase.query.filter_by(name=name).first()
            return str(testcase)
        else:
            testcases = TestCase.query.all()
            app.logger.info({'testcases': testcases})
            return [str(testcase) for testcase in testcases]

    def post(self):
        testcase = TestCase(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps"))
        )

        db.session.add(testcase)
        db.session.commit()

        testcases=TestCase.query.all()
        return [str(testcase) for testcase in testcases]

    def put(self):
        pass

    def delete(self):
        name = request.json['name']
        testcase=TestCase.query.filter_by(name=name).first()
        db.session.delete(testcase)
        testcases = TestCase.query.all()
        app.logger.info({'testcases': testcases})
        return [str(testcase) for testcase in testcases]

class Suite:
    pass

class SuiteService:
    pass


class ExcutionService(Resource):
    def post(self):
        testcase_id=request.json.get('testcase_id')
        jenkins.jobs['lagou5_testcase'].invoke(
            build_params={'testcase_id': testcase_id}
        )

class Result:
    pass

class ResultService:
    pass

class Report:
    pass



api.add_resource(TestCaseService, '/testcase')
api.add_resource(ExcutionService, '/execution')

if __name__ == '__main__':
    app.run(debug=True)
