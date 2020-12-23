import pytest
from Class_test.Counter_demo import Counter

class TestCaseDemo:
    def setup_class(self):
        self.t = Counter()
        print('start')
    # def setup_teardown_class(self):
    #     print('end')
    @pytest.mark.parametrize('a,b,expect',[(1,2,3),(2,3,4)])
    def test_add(self,a,b,expect):
        result = self.t.add(a,b)
        assert result == expect
    # def test_case_minus(self,a,b,expect):
    #     pass
    # def test_case_multiply(self,a,b,expect):
    #     pass
    # def test_case_divide(self,a,b,expect):
    #     pass

