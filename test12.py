class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__acces = "user"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_acces(self):
        return self.__acces

    def set_name(self, name):
        self.__name = name

    def __repr__(self):
        return f"User(id={self.__id}, name='{self.__name}', acces='{self.__acces}')"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._User__acces = 'admin'  # Доступ через изменение защищённого атрибута базового класса

    def add_user(self, user_list, user):
        if user not in user_list:
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в список.")
        else:
            print(f"Пользователь {user.get_name()} уже в списке.")
        print(user_list)

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"Пользователь {user.get_name()} удалён из списка.")
        else:
            print(f"Пользователь {user.get_name()} не найден в списке.")
        print(user_list)


# Пример использования
users = []
user1 = User("11", "Кирилл")
user2 = User("12", "Марина")
user3 = User("13", "Карина")
user4 = User("14", "Виктория")
admin = Admin("123", "Дима")

print(user1.get_id())
print(user3.get_name())

admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, user3)
admin.add_user(users, user4)

admin.remove_user(users, user3)
admin.remove_user(users, user3)  # Попытка удалить уже удалённого пользователя
