class Human():
    hp = 100
    name = "기본 이름"

    def walk(self):
        print("I can walk")

class Wizard(Human):
    def __init__(self, name):
        self.name = name
    def magic(self):
        print("Magic!")

my_char = Wizard("황고명")
