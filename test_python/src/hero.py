from typing import List
from time import ctime
from test_python.src.log import log

def mylog(func):
    '''
    输出log
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        log.debug(f'{mylog.__name__}{func.__name__}')
        print(ctime())
        return func(*args, **kwargs)
    return wrapper


class Hero:
    hp = 100
    power = 10
    magic_hp = 200
    speed = 1

    @mylog
    def fight(self, hero: 'Hero'):
        while True:
            hero.hp -= self.power
            if self.winner(self, hero):
                return True
            self.hp -= hero.power
            if self.winner(hero, self):
                return False

    def winner(self, hero1, hero2):
        if hero1.hp <= 0:
            return False
        if hero2.hp <= 0:
            return True

    def fight_many(self, heros: List['Hero']):
        pass
