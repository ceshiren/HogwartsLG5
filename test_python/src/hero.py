
class Hero:
    hp=100
    power=10
    magic_hp=200
    speed=1
    tools=[]

def fight(self, hero: 'Hero'):
    while True:
        hero.hp -= self.power
        if self.winner(self, hero):
            return True
        self.hp -= hero.power
        if self.winner(hero,self):
            return False


def winner(self,hero1,hero2):
    print(f'{hero1} VS {hero2}')
    if hero1.hp <= 0:
        return False
        print(False)
    if hero2.hp <=0:
        return True
        print(True)

def fight_many(self, heros: list['Hero']):
    pass