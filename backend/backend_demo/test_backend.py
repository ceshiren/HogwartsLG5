import requests


def test_testcase_post():

    r=requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'id':10086,
            'name': "testcase wg",
            "steps": {"step":["step 1", "step 2"]}
        }
    )
    print(r.status_code)
    assert r.status_code == 200

    # r=requests.post(
    #     'http://127.0.0.1:5000/testcase',
    #     json={
    #         'name': "testcase 3",
    #         "steps": ["step 1", "step 2"]
    #     }
    # )
    # assert r.status_code == 200
    #
    # r = requests.delete(
    #     'http://127.0.0.1:5000/testcase',
    #     json={
    #         'name': "testcase 3"
    #     }
    # )
    # assert r.status_code == 200
