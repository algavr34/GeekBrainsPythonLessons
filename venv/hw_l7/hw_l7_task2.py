from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, size : int):
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    @abstractmethod
    def square(self):
        pass

    @property
    def summa(self):
        return f"Размер нашей одежды: {self.size} квадратных метров"


class Coat(Clothes):
    def square(self):
        return self.size / 6.5 + 0.5

class Suit(Clothes):
    def square(self):
        return 2 * self.size + 0.3

our_coat = Coat(40)
our_suit = Suit(55)
print(f"Для пошива пальто нужно {our_coat.square() :.2f} метров ткани, "
      f"Для пошива костюма нужно {our_suit.square() :.2f} метров ткани, "
      f"Всего нужно {our_coat.square() + our_suit.square() :.2f} метров ткани")