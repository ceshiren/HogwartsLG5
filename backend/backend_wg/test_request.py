import  requests

def test_testcase_post():
    r=requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'id':1,
            'name':'testcase1',
            'steps':['step1','step2']
        }
    )
    print(r.json())
    assert r.status_code == 200;

def test_testcase_delete():
    r=requests.delete(
        'http://127.0.0.1:5000/testcase',
        json={
            'name':'testcase2',
            'steps':['step1','step2']
        }
    )
    print(r.json())
    assert r.status_code == 200;


def test_testcase_put():
    r = requests.put(
        'http://127.0.0.1:5000/testcase?name=testcase1',
        json={
            'name': 'testcase1',
            'steps': ['step3', 'step4']
        }
    )
    print( r.json())
    assert r.status_code == 200;

def test_testcase_get():
    r = requests.get(
        'http://127.0.0.1:5000/testcase?name=testcase1',
    )
    print( r.json())
    assert r.status_code == 200;

