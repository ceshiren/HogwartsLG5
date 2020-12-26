import pytest


class Test_Demo:
    @pytest.mark.smoke
    #smoke为(标签名)
    def test_one(self):
        assert  1==1

    @pytest.mark.smoke
    @pytest.mark.demo
    def test_two(self):
        assert  1==1