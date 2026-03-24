from abc import ABC, abstractmethod

# abstraktne klass- ei lase sellest klassist objekte luua
# kohustab lapsklassis abstraktseid meetodeid üle kirjutama
# abstraktne klass sisaldab *vähemalt* üht või enamat abstraktset meetodit

class Vehicle():
    @abstractmethod

    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("sa sõidad autoga")

    def stop(self):
        print("auto peatus")

class Motorcycle(Vehicle):
    def go(self):
        print("sa sõidad tsikliga")

    def stop(self):
        print("tsikkel jäi seisma")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Here is your sprinklid")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Lisad fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} jäätis")

get_ice_cream("vanilje")

class Rectangle:
    def __init__(self, width, height):
        self._width = width  # loome kaitstud atribuudi width ja height
        self._height = height

    @property  # @property dekoraator on siin getter meetod kaitstud atribuutidele ligipääsemiseks
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

        else:
            print("laius peab olema suurem kui 0")

    @height.setter  # setter meetod kaitstud atribuutide muutmiseks võimaldab teha lisaloogikat
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height

        else:
            print("kõrgus peab olema suurem kui 0")


    @width.deleter
    def width(self):
        del self._width
        print("kustutasin laiuse")

    @height.deleter
    def height(self):
        del self._height
        print("kustutasin kõrguse")

rectangle = Rectangle(3,4)
rectangle.width = 5
rectangle.height = -1
del rectangle.width
del rectangle.height


#print(rectangle._width)  # otse _width printides saan hoiatuse kaitstud atribuudi kohta
#print(rectangle.height)   # kutsume @property abil tehtud getter meetodi välja

# @property aitab luua getter meetodi kaitstud / privaatsetele atribuutidele ligipääsemiseks