
class Hero:
    hp = 100
    power =10
    magic_hp = 200
    speed =1
    tools = []

    def fight(self,hero:'Hero'):
        while True:
            hero.hp -= self.power
            if hero.hp <= 0:
                return True
            self.hp -= hero.power
            if self.hp <= 0:
                return False

