from menu import *
from classes_functions import *

#Init game
game_menu()

size_of_board, number_of_ships, player_dict = get_params_from_user()

game = init_game(size_of_board, number_of_ships, player_dict)


#Game loop
while(True):

    if (): # no more players alive or interuppet
        #return to menu
        ...

    turn_of_one_player()






