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
        print('+' * (self.col+2))
        for self.r in self.field:
            print('+', end='')
            for self.c in self.r:
                if self.c != ' ':
                    print('#', end='')
                else:
                    print(self.c, end='')
            print('+')
        print('+' * (self.col + 2))

    def install(self, klass):
        self.c = random.randint(0, self.col-1)
        self.r = random.randint(0, self.raw-1)
        self.field[self.r][self.c] = klass(self.col, self.raw)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == '__main__':
    dish = Dish(5, 10)
    dish.install(Cell)
    dish.draw()
