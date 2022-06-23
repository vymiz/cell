from field import Dish
from cell import Cell
from clone import *
import os, sys
import time

dish = Dish(10, 25)
dish.install(Prey, 'o')
dish.install(Predator, '+')
os_type = sys.platform

while True:
    if os_type == 'win32':
        os.system('cls')
    elif os_type == 'darwin':
        os.system('clear')

    dish.draw()
    time.sleep(1)
    dish.process()
