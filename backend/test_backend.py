import requests


def test_testcase_post():

    r=requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 2",
            "steps": ["step 1", "step 2"]
        }
    )
    assert r.status_code == 200

    r=requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 3",
            "steps": ["step 1", "step 2"]
        }
    )
    assert r.status_code == 200

    r = requests.delete(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 3"
        }
    )
    assert r.status_code == 200

def test_execution():
    r=requests.post(
        'http://127.0.0.1:5000/execution',
        json={
            'testcase_id': 1
        }
    )
    assert r.status_code == 200

