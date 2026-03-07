class Person:
    number_of_people = 0  # terve klassi atribuut, sest pole defineeritud meetodis ja puudub ligipääs klassi objektidele
    GRAVITY = -9.8  #klassi konstandid on mõttekas defineerida klassi sees

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod  # muudab klassi ennast, ei pääse ligi objektidele
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Raiko")
p2 = Person("Mall")

print(Person.number_of_people)
print(p1.number_of_people)
Person.number_of_people = 8
print(p2.number_of_people)  # prindib 8. p2 on klassi objekt, kuid objektil pole atribuuti number.., seega muudab klassi atribuuti
print(Person.number_of_people_())

class Math:
    @staticmethod  # neil pole ligipääsu objektidele, klass on üldiseks kasutamiseks
    def add5(x):
        return x + 5
    @staticmethod
    def pr():
        print("run")

        pass

print(Math.add5(5))
Math.pr()

class Language:
    def say_hello(self):
        raise NotImplementedError("palun kasuta say_hello funktsiooni child klassis")

class French(Language):

    def say_hello(self):
        print("Bonjour")

class Chinese(Language):
    def say_hello(self):
        print("你好")

def intro(lang):  # meetod, mis tervitab vastavalt sellele, mis klassist objekt on
    lang.say_hello()  # intro meetod ei tea objektist midagi, kuid eeldab, et objektil on say_hello() meetod

timbu = French()  # timbu on objekt klassist French
limbu = Chinese()  # limbu on objekt klassist Chinese

intro(timbu)
intro(limbu)