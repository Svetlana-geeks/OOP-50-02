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
        print(f"{self.name} берет паузу")

from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def unique_attac(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass

    def attack(self):
        print(f"{self.name} атакует!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает!")

    def action(self):
        random_number = self.get_random_int()
        if random_number == 1:
            self.attack()
        elif random_number == 2:
            self.protection()
        else:
            self.rest()

    class Jester(Hero):
        def unique_attack(self):
            print("кидает камень!")

        def unique_scream(self):
            print("смех")