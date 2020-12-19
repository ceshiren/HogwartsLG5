import unittest
from unittest import TestCase
from test_python.src.hero_factory import HeroFactory


class TestHero(TestCase):
    def test_fight(self):
        chengyaojin = HeroFactory.creat_hero('chengyaojin')
        libai = HeroFactory.creat_hero('libai')
        assert chengyaojin.fight(libai) == True
        chengyaojin = HeroFactory.creat_hero('chengyaojin')
        libai = HeroFactory.creat_hero('libai')
        assert libai.fight(chengyaojin) == False

if __name__ == '__main__':
    unittest.main()