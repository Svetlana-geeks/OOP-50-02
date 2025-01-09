class Heroes :
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action (self):
        return print(f"({self.name} делает удар мечом")

    def attack (self):
        return print(f"({self.name} атакует слева")

