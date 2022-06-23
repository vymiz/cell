from cell import Cell
import random

class Predator(Cell):

    def __call__(self, field):
        self.ctr += 1
        if self.ctr >= 100:
            self.apoptos(field)
        self.empty_check(field)

        self.move(field)

        if self.busy_field is not None:
            self.kill(field)


class Prey(Cell):

    def __call__(self, field):
        self.ctr += 1
        if self.ctr >= random.randint(10, 50):
            self.apoptos(field)
        self.empty_check(field)

        if len(self.empty_arr) in range(2, 6): self.apoptos(field)  # if fthe field is overcrowded cell dies

        self.choice = random.randint(1, 3)
        if self.choice == 1:
            self.move(field)
        elif self.choice == 2 or 3:
            self.mitosis(field)