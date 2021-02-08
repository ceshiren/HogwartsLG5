#coding:utf-8
from test_python.src.log import *
def logs(func):
    def wrapper(*args,**kwargs):
        log.debug(f'{log.__name__}--->{func.__name__}')
        log.debug(f'打印log的func返回：{func(*args,**kwargs)}')
        return  func(*args,**kwargs)
    log.debug(f'打印装饰器主方法返回的值：{wrapper}')
    return wrapper

class Hero:
    hp = 100
    power = 20
    magic_hp = 200
    speed = 1

    @logs
    def fight(self,hero):
        while True:
            hero.hp -= self.power
            log.debug(f'打印对方英雄血量{hero.hp}')
            if self.winner(self,hero):
                return True
            self.hp -= hero.power
            log.debug(f'打印自己血量{self.hp}')
            if self.winner(hero,self):
                return False

    @logs
    def winner(self,hero1,hero2):
        log.debug(f'{hero1.name}VS{hero2.name}')
        if hero1.hp <=0:
            log.debug('自己已死')
            return False
        if hero2.hp <=0:
            log.debug('对方已死')
            return True

'''
    def fight_many(self,heros:list["Hero"]):#通过声明list，知道这个heros英雄，h就可以识别类型了
        for h in heros:
            h.
'''