from unittest import TestCase

from test_python.src.ChengYaoJin import ChengYaoJin
from test_python.src.hero_factory import HeroFactory
from test_python.src.libai import LiBai


class TestHero(TestCase):
    def test_fight(self):
        chengyaojin = ChengYaoJin()
        libai = LiBai()
        assert chengyaojin.fight(libai) == True


        # chengyaojin = ChengYaoJin()
        # libai = LiBai()
        HeroFactory.create_hero('程咬金')
        HeroFactory.create_hero(('李白'))
        assert libai.fight(chengyaojin) == False