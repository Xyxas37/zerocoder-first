import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power // 2, self.attack_power)
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанес {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        print(f"{self.player.name} против {self.computer.name}")
        print("-" * 30)

        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {max(self.computer.health, 0)} здоровья.")
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            print("-" * 30)


            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {max(self.player.health, 0)} здоровья.")
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

            print("-" * 30)

        print("Игра окончена!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()