# Инкапсуляция

# Открытые
# Защищенные (Protected) | -
# Приватный (Private) | __


import random

# class Hero:

#     def __init__(self, name, hp, lvl):
#         self.name = name
#         self.hp = hp
#         self.lvl = lvl
#         self._luck = random.randint(0, 100)
#         self.__crit_dmg = random.randint(0, 100)
#
#     def __heal_hp(self):
#         return random.randint(0, 100)
#
#     def rest(self):
#         self.hp += self.__heal_hp()
#
#     def defence(self):
#         if self._luck >= 20:
#             return print (f"{self.name} успешно защищается")
#         else:
#             return print(f"{self.name} не смог защититься")
#
#     def attack(self):
#         if self.__crit_dmg >= 30:
#             return print (f"{self.name} крит атака")
#         else:
#             return print(f"{self.name} базовая атака")
#
# kirito = Hero("Kirito", 100, 1)
#
# #print(kirito._luck)
# print(dir(kirito)) #можно увидеть все защищенные элементы
# print(kirito._Hero__crit_dmg)
# print(kirito._Hero__heal_hp())


from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self._luck = random.randint(0, 100)
        self.__crit_dmg = random.randint(0, 100)

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def attack(self):
        pass

class Magichero(Hero):
    def action(self):
        pass
    def attack(self):
        pass

gendalf = Magichero ("Test", 100, 1)