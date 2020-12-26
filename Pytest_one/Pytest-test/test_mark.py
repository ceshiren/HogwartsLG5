import pytest
class Test_Demo:

    ##在方法上打上标签名,且可以同时在一个方法上打多个标签
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_one(self):
        assert 1 == 1

    @pytest.mark.demo
    def test_two(self):
        assert 2 == 1

