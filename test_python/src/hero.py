from typing import List

from test_python.src.log import log


def log_decorator(func):
    """
    func=winner
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        log.debug(f'{log_decorator.__name__} --> {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


class Hero:
    hp = 100
    power = 10
    magic_hp = 200
    speed = 1
    tools = []

    @log_decorator
    def fight(self, hero: 'Hero'):
        while True:
            hero.hp -= self.power
            if self.winner(self, hero):
                return True
            self.hp -= hero.power
            if self.winner(hero, self):
                return False

    @log_decorator
    def winner(self, hero1, hero2):
        log.debug(f'{hero1} VS {hero2}')
        if hero1.hp <= 0:
            log.debug('False')
            return False
        if hero2.hp <= 0:
            log.debug('True')
            return True

    def fight_many(self, heros: List['Hero']):
        pass
