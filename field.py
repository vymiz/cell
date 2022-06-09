import random
from cell import Cell


class Dish:

    def __init__(self, raw, col):
        self.raw = raw
        self.col = col
        self.field = []
        for self.r in range(self.raw):
            self.tmp = []
            for self.c in range(self.col):
                self.tmp.append(' ')
            self.field.append(self.tmp)

    def draw(self):
        print()
        print('+','-' * self.col, '+', sep='')
        for self.r in range(self.raw):
            print('|', end='')
            for self.c in range(self.col):
                print(self.field[self.r][self.c], end='')
            print('|')
        print('+','-' * self.col, '+', sep='')

    def install(self, klass):
        self.c = random.randint(0, self.col - 1)
        self.r = random.randint(0, self.raw - 1)
        self.field[self.r][self.c] = klass(self.r, self.c)

    def process(self):
        for self.r in range(self.raw):
            for self.c in range(self.col):
                if self.field[self.r][self.c] != ' ':
                    self.field[self.r][self.c](self.field)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == '__main__':
    dish = Dish(3, 4)
    dish.install(Cell)
    dish.draw()
    print(dish.field)
    dish.process()
    dish.draw()
    print(dish.field)
    dish.process()
    dish.draw()
    print(dish.field)
    # print(dish.field)
