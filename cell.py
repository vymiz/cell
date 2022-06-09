import random, copy


class Cell:

    def __init__(self, raw, col):
        self.col = col
        self.raw = raw
        self.ctr = 1
        self.img = '#'
        # TMP VARS:
        # Vars for empty_check func:
        self.tmp_c = None
        self.tmp_r = None
        self.empty_arr = None
        self.empty_field = None

    def __str__(self):
        return self.img

    def apoptos(self, field):
        field[self.raw][self.col] = ' '

    def empty_check(self, field):
        self.empty_arr = []  # empty tmp arr
        for self.r in range(-1, 2):  # run through raws
            for self.c in range(-1, 2):  # run through cols
                if self.r != 0 or self.c != 0:  # exclude zero variants
                    self.tmp_r = self.raw + self.r  # get coordinats of possibly empty field
                    self.tmp_c = self.col + self.c
                if 0 <= self.tmp_r < len(field):  # check array's borders
                    if 0 <= self.tmp_c < len(field[0]):
                        self.tmp_tuple = (self.tmp_r, self.tmp_c)  # assemble coordinates ia tuples
                        if self.tmp_tuple not in self.empty_arr:  # erase duplicates which get here from nothing
                            if field[self.tmp_r][self.tmp_c] == ' ':  # check is this field empty?
                                self.empty_arr.append(self.tmp_tuple)
        # print(self.empty_arr)
        if len(self.empty_arr) == 0:
            self.empty_field = None
        elif len(self.empty_arr) == 1:
            self.empty_field = self.empty_arr[0]
        else:
            self.empty_field = random.choice(self.empty_arr)

    def move(self, field):
        if self.empty_field != None:
            self.r = self.empty_field[0]
            self.c = self.empty_field[1]
            field[self.r][self.c] = copy.copy(self)
            # field[self.raw][self.col] = ' '
            self.apoptos(field)

    def __call__(self, field):
        self.ctr += 1
        if self.ctr > 3:
            self.apoptos(field)
        self.empty_check(field)
        self.move(field)
        # print(self.empty_field)
        # print(field)


if __name__ == '__main__':
    pass
