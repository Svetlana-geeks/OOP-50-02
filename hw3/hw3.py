from main import Hero

class Jester(Hero):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)

    def unique_attack(self):
        print(f"{self.name} бросает тухлое яйцо!")

    def unique_scream(self):
        print(f"{self.name} смеется!")


jester = Jester("John", 10, 50)
print(jester.name)  # Выведет: john
jester.attack()  # Вызовет метод attack из класса Hero
jester.unique_scream()
jester.unique_attack()
jester.rest()
jester.protection()
