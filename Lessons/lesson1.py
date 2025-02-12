#OOP

#First Class

#add_number
#AddNumber

# Класс
class Person:

    # Магический метод
    def __init__(self, name, age=0, city="None"):
        # Атрибуты класса
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}, я живу в городе {self.city}")

    def __str__(self):
        return f'Вернул имя объекта {self.name}'
# Объекты класса /экземпляры класса
person_first = Person("Ардагер", 25,"с.Сокулук")
person_second = Person("John Doe", 33,"None")

print(person_first.age)
person_first.introduce()
print(person_second)