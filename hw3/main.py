import random

class Hero:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp
        self.__random_int = random.randint(1, 3)  # Приватный атрибут

    def get_random_int(self):
        return self.__random_int

    def attack(self):
        print(f"{self.name} атакует!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает!")

        from abc import ABC, abstractmethod

        class Hero(ABC):
            # (оставшаяся часть класса)

            @abstractmethod
            def unique_attack(self):
                pass

            @abstractmethod
            def unique_scream(self):
                pass


