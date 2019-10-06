from classes_functions import *

game = Game()
a= game.init_board(2,5)
print(a)


import numpy as np


array = np.zeros([5,5])
ship={}

class ship(object):
    def __init__(self):
        self.locations = []

s= ship()
s.locations =  [(1,1),(1,2)]

def change_locations(some_num,locations,array):
    for i in locations:
        array[i] = some_num

change_locations(1, s.locations,array)

array



