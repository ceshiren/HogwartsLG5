import pytest
@pytest.fixture(scope='session')
def login():
    print('登录成功***')
    user = 'shen'
    pawd = 'gang'
    yield [user,pawd]
    print('退出登录***')