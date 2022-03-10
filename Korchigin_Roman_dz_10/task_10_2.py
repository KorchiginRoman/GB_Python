from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    @property
    def calculate(self):
        return f'{self.cloth / 6.5 + 0.5 :.2f}'


class Costume(Clothes):
    @property
    def calculate(self):
        return f'{2 * self.cloth + 0.3:.2f}'


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
