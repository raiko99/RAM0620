class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"olen {self.name} ja olen {self.age} aastane")

    def speak(self):
        print("mdea mis häält ma teen")

class Cat(Pet):  # klass Cat pärib meetodid ja atribuuddid Pet klassist.

    def __init__(self, name, age, color):  # teen alamklassi oma __init__ millel on teised atribuudid
        super().__init__(name, age)  # pärime vanemklassi init meetod
        self.color = color

    def speak(self):
        print("mjäu")

    def show(self):
        print(f"olen {self.name}, {self.age} aastane ja {self.color} värvi")

class Dog(Pet):

    def speak(self):
        print("auh!")


class Fish(Pet):
    pass

p = Pet("Pontu", 10)
p.show()
p.speak()
k = Cat("Miisu", 5, "punane")  # k on klassi Cat objekt, klass pärib oma meetodid Pet klassist
k.show()
k.speak()  # lapsklassi meetod kirjutab üle päritud klassi meetodid
m = Dog("Muri", 8)
m.show()
m.speak()
f = Fish("Kallu",1)
f.speak()


"""
Cat(Pet) tähendab, et klass Cat pärib __init__ ja teised meetodid klassist Pet
lapsklassi meetod kirjutab üle päritud klassi meetodid
lapsklassil võiv olla oma __init__ meetod, kus on teised atribuudid
"""