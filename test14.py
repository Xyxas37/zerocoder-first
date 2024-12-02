from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword (Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

class Bow (Weapon):
    def attack(self):
        print("Боец наносит удар из лука")

class Fighter():
    def __init__(self, weapon:Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon:Weapon):
        self.weapon = weapon

    def fight(self, monster):
        print(f"Боец выбирает {self.weapon.__class__.__name__.lower()}.")
        attack_message = self.weapon.attack()
        print(attack_message)
        monster.receive_damage()

class Monster():
    def __init__(self):
        self.health = 1  # У монстра 1 единица здоровья

    def receive_damage(self):
        print("Монстр побежден!")


sword = Sword()
bow = Bow()

fighter = Fighter(sword)
monster = Monster()

fighter.fight(monster)
fighter.changeWeapon(bow)
fighter.fight(monster)