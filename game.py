class Enemy:
    name = ""
    lives = 0
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            print(self.name + 'killed')
        else:
            print(self.name + 'has' + str(self.lives) + 'lives')

class Monster(Enemy):
    def __init__(self, name, lives):
        super().__init__(name, lives)

class Alien(Enemy):
    def __init__(self, name, lives):
        super().__init__(name, lives)

m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break
    elif x == 'laser':
        a.hit()
    else:
        m.hit()