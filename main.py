from field import Dish
from cell import Cell
import os, sys
import time

dish = Dish(10, 25)
dish.install(Cell, 'o')
dish.install(Cell, '+')
os_type = sys.platform

while True:
    if os_type == 'win32':
        os.system('cls')
    elif os_type == 'darwin':
        os.system('clear')

    dish.draw()
    time.sleep(1)
    dish.process()
