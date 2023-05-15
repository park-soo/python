class Char:
    def __init__(self, name, ):
        self.name = name

    def do(self):
        print("do")


class Healer(Char):
    def do(self):
        print("healing")


class Fighter(Char):
    def do(self):
        print("fight")


class Wizard(Char):
    def do(self):
        print("magic")


fighter1 = Fighter("Tom")
healer1 = Healer("Andy")
wizard1 = Wizard("Emily")

for x in (fighter1, healer1, wizard1):
    print(x.name)
    x.do()
