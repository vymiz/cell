class Cell:

    def __init__(self, raw, col):
        self.col = col
        self.raw = raw
        self.ctr = 1
        self.img = '#'
        # TMP VARS:
        #Vars for empty_check func:
        self.tmp_c = None
        self.tmp_r = None
        self.empty_arr = None


    def __str__(self):
        return self.img

    def apoptos(self, field):
        field[self.raw][self.col] = ' '

    def empty_check(self, field):
        self.empty_arr = []
        for self.r in range(-1,2):
            for self.c in range(-1,2):
                if self.r != 0 or self.c != 0:
                    self.tmp_r = self.raw + self.r
                    self.tmp_c = self.col + self.c
                if 0 <= self.tmp_r < len(field):
                    if 0 <= self.tmp_c < len(field[0]):
                        self.tmp_tuple = (self.tmp_r, self.tmp_c)
                        if self.tmp_tuple not in self.empty_arr:
                            self.empty_arr.append(self.tmp_tuple)
        print(self.empty_arr)


    def test(self, field):
        print(len(field))
        print(len(field[0]))
        print()


    def __call__(self, field):
        # self.ctr += 1
        # if self.ctr > 10:
        #     self.apoptos(field)
        # self.test(field)
        self.empty_check(field)


if __name__ == '__main__':
    pass
