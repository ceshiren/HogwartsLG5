import pytest,requests
from requests_work2.common.base import Api
from requests_work2.common.member_req import Member

class TestApi:

    def setup_class(self):
        self.member = Member()

    def test_del_member(self):
        userid = 'shenggg'
        #新增成员
        res = self.member.add_member(userid,'沈刚11','17799999999',[1])
        pytest.assume(res.get('errmsg','新增失败') == 'created')
        #查询成员
        res = self.member.get_member(userid)
        pytest.assume(res.get('userid', '找不到user_id') == userid)
        #删除成员
        self.member.del_member(userid)
        #查询成员
        res = self.member.get_member(userid)
        pytest.assume(res.get('errcode', '找不到user_id') == 60111)

if __name__ == '__main__':
    pytest.main(['test_request.py','-sq'])
