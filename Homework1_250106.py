# Класс

class Hero:

    # Магический метод
    def __init__(self, name, lvl=0, HP=0):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10


    def __str__(self):
        return f' Имя: {self.name}, lvl {self.lvl}, HP: {self.HP}'


# Объекты класса /экземпляры класса
hero_first = Hero ("Fantom", 5, 10)
hero_second = Hero ("Saturn", 33,15)
hero_third = Hero ("Edgar", 6, 8)
hero_forth = Hero ("Mars", 40,5)


hero_first.introduce()
print(f'мой уровень равен или выше 10: {hero_first.is_adult()} ')

hero_second.introduce()
print(f'мой уровень равен или выше 10: {hero_second.is_adult()} ')

print(hero_third)
print(hero_forth)