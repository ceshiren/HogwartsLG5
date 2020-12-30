import pytest

from test_calculator_作业2.Calculator import Calculator

@pytest.fixture(scope="module")
def get_cal():
    calc = Calculator()
    return calc

@pytest.fixture(scope="module")
def setup_cal():
    print("开始计算")

@pytest.fixture(scope="module")
def teardown_cal():
    print("\n计算结束")