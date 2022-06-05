from field import Dish
from cell import Cell
import os
import time

dish = Dish(3, 6)
dish.install(Cell)

while True:
    dish.draw()
    time.sleep(1)
    dish.process()
    os.system('cls')
