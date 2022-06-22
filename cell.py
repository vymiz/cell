import random, copy


class Cell:

    def __init__(self, raw, col, img):
        self.col = col
        self.raw = raw
        self.ctr = 1
        self.img = img
        # TMP VARS:
        # Vars for empty_check func:
        self.tmp_c = None
        self.tmp_r = None
        self.empty_arr = None
        self.empty_field = None
        self.busy_arr = None
        self.busy_field = None
        self.r = None
        self.c = None
        # Vars for Mitosis func:
        self.trigger = True
        self.choice = None

    def __str__(self):
        return self.img

    def apoptos(self, field):
        field[self.raw][self.col] = ' '

    def empty_check(self, field):
        self.empty_arr = []  # empty empty arr
        self.busy_arr = []  # empty busy arr
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
                                self.empty_arr.append(self.tmp_tuple)  # if the field is empty is added into arr
                            elif field[self.tmp_r][self.tmp_c] != self.img:
                                # select field to kill func
                                self.busy_arr.append(self.tmp_tuple)
        # select the field to move
        if len(self.empty_arr) == 0:
            self.empty_field = None
        elif len(self.empty_arr) == 1:
            self.empty_field = self.empty_arr[0]
        else:
            self.empty_field = random.choice(self.empty_arr)

        # select the field to kill
        if len(self.busy_arr) == 0:
            self.busy_field = None
        elif len(self.busy_arr) == 1:
            self.busy_field = self.busy_arr[0]
        else:
            self.busy_field = random.choice(self.busy_arr)

    def mitosis(self, field):
        self.trigger = not self.trigger
        if self.empty_field is not None and self.trigger:
            self.r = self.empty_field[0]
            self.c = self.empty_field[1]
            field[self.r][self.c] = self.__class__(self.r, self.c, self.img)
        if self.empty_field is None:
            self.apoptos(field)

    def move(self, field):
        self.trigger = not self.trigger
        if self.empty_field is not None and self.trigger:
            self.r = self.empty_field[0]
            self.c = self.empty_field[1]
            field[self.r][self.c] = self.__class__(self.r, self.c, self.img)
            field[self.r][self.c].ctr = self.ctr
            self.apoptos(field)

    def kill(self):
        pass  # TODO

    def __call__(self, field):
        self.ctr += 1
        if self.ctr >= random.randint(10, 50):
            self.apoptos(field)
        self.empty_check(field)

        if len(self.empty_arr) in range(2, 6): self.apoptos(field)  # if fthe field is overcrowded cell dies

        self.choice = random.randint(1, 2)
        if self.choice == 1:
            self.move(field)
        elif self.choice == 2:
            self.mitosis(field)


if __name__ == '__main__':
    pass
