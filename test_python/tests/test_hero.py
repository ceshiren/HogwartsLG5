from unittest import TestCase
from test_python.src.chengyaojin import ChengYaoJin
from test_python.src.libai import LiBai


class Test(TestCase):
    def test_hero(self):
        chengyaojin = ChengYaoJin()
        libai = LiBai()
        assert chengyaojin.fight(libai) == True
        assert libai.fight(chengyaojin) == False
