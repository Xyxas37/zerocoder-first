#Задание
#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

#Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
#В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self, food):
        print(f"{self.name} ест {food}.")

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"


# 2. Подклассы Bird, Mammal и Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wing_span} метров.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")

    def run(self):
        print(f"{self.name} быстро бежит.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

    def crawl(self):
        print(f"{self.name} ползет медленно.")


# 3. Полиморфизм: функция для воспроизведения звуков
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# 4. Класс Zoo для композиции
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal}")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен сотрудник: {staff_member}")

    def show_animals(self):
        print("Список животных в зоопарке:")
        for animal in self.animals:
            print(animal)

    def show_staff(self):
        print("Список сотрудников в зоопарке:")
        for staff_member in self.staff:
            print(staff_member)


# 5. Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal, food):
        print(f"{self.name} кормит {animal.name} {food}.")

    def __repr__(self):
        return f"ZooKeeper(name='{self.name}')"


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

    def __repr__(self):
        return f"Veterinarian(name='{self.name}')"


# Пример использования
if __name__ == "__main__":
    # Создание животных
    parrot = Bird("Попугай", 2, 0.5)
    lion = Mammal("Лев", 5, "золотой")
    snake = Reptile("Змея", 3, "чешуйчатая")

    # Создание сотрудников
    zookeeper = ZooKeeper("Анна")
    vet = Veterinarian("Дмитрий")

    # Создание зоопарка
    zoo = Zoo("Городской Зоопарк")

    # Добавление животных и сотрудников
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    zoo.add_staff(zookeeper)
    zoo.add_staff(vet)

    # Демонстрация функций
    zoo.show_animals()
    zoo.show_staff()

    # Полиморфизм: звуки животных
    print("\nЗвуки животных:")
    animal_sound(zoo.animals)

    # Действия сотрудников
    print("\nДействия сотрудников:")
    zookeeper.feed_animal(lion, "мясо")
    vet.heal_animal(snake)
