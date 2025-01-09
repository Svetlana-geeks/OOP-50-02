class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} прыгнул вперед")

    def attack(self):
        print(f"{self.name} ударил ногой!")

import random
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1
        if self.arrows < 0:
            print("У вас закончились стрелы!")
            return
        if random.random() < self.precision:
            print(f"{self.name} успешно атаковал стрелой!")
        else:
            print(f"{self.name} промахнулся!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил колчан. Теперь у вас {self.arrows} стрел.")

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.hp}")
        print(f"Стрелы: {self.arrows}")
        print(f"Точность: {self.precision}")

# Создание экземпляра класса и вызов методов
Voin = Archer("Воин", 100, 20, 0.8)
Voin.action()
Voin.attack()
Voin.rest()
Voin.status()