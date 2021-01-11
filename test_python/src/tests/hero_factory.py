from test_python.src.tests.chengyaojin import ChengYaoJin
from test_python.src.tests.hero import Hero
from test_python.src.tests.libai import LiBai
from test_python.src.tests.log import log


class HeroFactory:
    @classmethod
    def create_hero(cls, name: str) -> Hero:
        if name == '程咬金':
            return ChengYaoJin()
        elif name == "李白":
            return LiBai()
        else:
            log.error(f"don't know how to create hero {name}")
            return None
