from abc import ABC, abstractmethod
import random

class Tegelane(ABC):
    @abstractmethod
    def __init__(self, nimi:str, elu:int, võta_kahju:int):
        self._nimi = nimi
        self._elu = elu
        self._võta_kahju = võta_kahju

    @property
    def kahju(self, kogus):
        pass

    def on_elus(self):
        return True

    def seisund(self):
        pass

    @abstractmethod
    def ründa(self, vastane):
        pass


class Laulik(Tegelane):
    def __init__(self, nimi):
        super().__init__(self, nimi, 70)
    pass


class Kirjanik(Tegelane):
    def __init__(self, nimi):
        super().__init__(self, nimi, 100)

    pass


class Kriitik(Tegelane):
    def __init__(self, nimi):
        super().__init__(self, nimi, 120)

    pass


def lahing(t1, t2):
    pass


def main():
    t1 = Kriitik(nimi = "Mihkel")
    print(t1.nimi)


if __name__ == '__main__()':
    main()