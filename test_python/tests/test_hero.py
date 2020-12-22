from unittest import TestCase
from test_python.src.chengyaojin import CYJ
from test_python.src.libai import LiBai
from test_python.src.hero_factory import *

class TestHero(TestCase):
    def test_fight(self):
        # cyj = CYJ()
        # lb = LiBai()
        cyj = HeroFactory.creaet_hero("程咬金")
        lb = HeroFactory.creaet_hero('李白')
        assert cyj.fight(lb) == True
        print('**************重新开打***************')
        # cyj = CYJ()
        # lb = LiBai()
        cyj = HeroFactory.creaet_hero('程咬金')
        lb = HeroFactory.creaet_hero('李白')
        assert lb.fight(cyj) == False
