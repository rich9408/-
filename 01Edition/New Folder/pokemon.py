import random

class Pokemon():
    def __init__(self,name,lv):
        self.name =name
        self.lv = lv
        self.hp = lv * random.randint(15,18)
        self.power = lv * random.randint(4,7)
        
    def info(self):
        print(f"{self.name}/{self.hp}/{self.power}")
    def attack(self, enemy):
        enemy.hp -= self.power
        print(f"{enemy.name}의 체력 : {enemy.hp}")
        if enemy.hp <= 0:
            print(f"{enemy.name}(이)가 쓰러졌다.")
            
pikachu = Pokemon("피카츄", 20)
pikachu.info()
kkobugi = Pokemon("꼬부기", 20)
kkobugi.info()

while kkobugi.hp > 0 and pikachu.hp > 0:
    kkobugi.attack(pikachu)
    pikachu.attack(kkobugi)