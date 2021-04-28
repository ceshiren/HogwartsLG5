import pytest
class Test_Demo:
    # 给test_one用例添加smoke标签
    # 在测试用例/测试类前加上：@pytest.mark.标记名
    @pytest.mark.smoke
    def test_one(self):
        assert 1==1

    # 给test_two用例添加smoke和demo标签
    # 运行pytest -m "smoke or demo" 文件名
    @pytest.mark.smoke
    @pytest.mark.demo
    def test_two(self):
        assert 1==1