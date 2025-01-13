import random
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self._luck = random.randint (1,3)
        self.__random_int = random.randint(1, 3)  # Приватный атрибут, генерируется при создании объекта

    def get_random_int(self):
        return self.__random_int  # Метод для получения значения приватного атрибута

    def attack(self):
        print(f"{self.name} атакует!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает!")