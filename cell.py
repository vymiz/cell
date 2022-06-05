import random

class Cell:

    def __init__(self, raw, col):
        self.col = col
        self.raw = raw
        self.ctr = 1
        self.img = '#'

    def __str__(self):
        return self.img

    def apoptos(self, klass):
        self.img = ' '
        klass.field[self.raw][self.col] = ' '

    def __call__(self, klass):
        self.apoptos(klass)


if __name__ == '__main__':
    x = Cell(10, 10)
    print(x)
    # x.__del__()
    x = x()
    print(x)