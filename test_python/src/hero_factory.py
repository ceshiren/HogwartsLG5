from test_python.src.chengyaojin import *
from test_python.src.libai import *
from test_python.src.log import *
class HeroFactory:
    @classmethod
    def creaet_hero(cls,name:str):
        if name == '程咬金':
            return CYJ()
        elif name == '李白':
            return LiBai()
        else:
            log.error(f'不知道是哪个英雄{name}')
            return None