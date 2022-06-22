from field import Dish
from cell import Cell
import os, sys
import time

dish = Dish(10, 25)
dish.install(Cell, '.')
dish.install(Cell, '*')

while True:
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'darwin':
        os.system('clear')

    dish.draw()
    time.sleep(.5)
    dish.process()
