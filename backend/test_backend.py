import requests
from flask import request

from backend import app, TestCase, db


def test_get():

    name = request.args.get('name', None)
    app.logger.info({'name': name})
    if name:
        testcase = TestCase.query.filter_by(name=name).first()
        return str(testcase)
    else:
        testcases = TestCase.query.all()
        app.logger.info({'testcases': testcases})
        return [testcase.as_dict() for testcase in testcases]

def test_testcase_post():
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 4",
            "steps": ["step 1", "step 2"]
        }
    )
    assert r.status_code == 200

    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 5",
            "steps": ["step 1", "step 2"]
        }
    )
    assert r.status_code == 200

    # r = requests.delete(
    #     'http://127.0.0.1:5000/testcase',
    #     json={
    #         'name': "testcase 3"
    #     }
    # )
    # assert r.status_code == 200

def test_suite_testcase_id():
    r = requests.post(
        'http://127.0.0.1:5000/suite',
        json={
            'name': 'suite 1',
            'testcases': [1, 2, 3]
        }
    )
    assert r.status_code == 200


def test_suite_testcase_filename():
    r = requests.post(
        'http://127.0.0.1:5000/suite',
        json={
            'name': 'suite 1',
            'testcases': 'test_python/tests/test_hero.py'
        }
    )
    assert r.status_code == 200

def test_execution():
    r = requests.post(
        'http://127.0.0.1:5000/execution',
        json={
            'suite_id': 3
        }
    )
    assert r.status_code == 200
