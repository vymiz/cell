import random

class Cell:

    def __init__(self, raw, col):
        self.col = col
        self.raw = raw
        self.ctr = 1
        self.img = '#'

    def __str__(self):
        return self.img

    def __del__(self):
        self.img = ' '

    def __call__(self):
        self.__del__()


if __name__ == '__main__':
    x = Cell(10, 10)
    print(x)
    # x.__del__()
    x = x()
    print(x)