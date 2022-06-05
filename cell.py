class Cell:

    def __init__(self, raw, col):
        self.col = col
        self.raw = raw
        self.ctr = 1
        self.img = '#'

    def __str__(self):
        return self.img

    def apoptos(self, field):
        field[self.raw][self.col] = ' '

    def __call__(self, field):
        self.apoptos(field)


if __name__ == '__main__':
    pass
