from test_python.src import log
from test_python.src.ChengYaoJin import ChengYaoJin
from test_python.src.hero import Hero
from test_python.src.libai import LiBai


class HeroFactory:
    @classmethod
    def creat_hero(cls, name) -> Hero:
        if name == 'chengyaojin':
            return ChengYaoJin()
        elif name == 'libai':
            return LiBai()
        else:
            return None

