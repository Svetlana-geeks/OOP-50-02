class Grandmother:
    def cook(self):
        print("Бабушка: кладет в еду острый перец.")

class Father(Grandmother):
    def cook(self):
        print("Папа: кладет в еду острый перец и щепотку лимона")

class Mother(Grandmother):
    def cook(self):
        print("Мама: кладет в еду острый перец и мяту.")

class You(Father, Mother):
    def cook(self):
        print("Я: кладу в еду острый перец, щепотку лимона, мяту и соевый соус.")
        super().cook()