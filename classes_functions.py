import numpy as np
from scipy.stats import  norm
from collections import defaultdict


                                ### Construct board ###

### Generate a ship attributes ###
#-------------------------------------------------#
def generate_ship_size(board_length, n_ships):
    # Returns ship size when constructing board

    board_size = board_length**2
    avg_ship_size = board_size/(n_ships*3)
    ship_size = norm.ppf(np.random.random(1), loc=avg_ship_size, scale=2).astype(int)[0]

    return ship_size

def generate_ship_direction():
    return np.random.randint(0,1)


def generate_ship_attributes(board_length, n_ships):

    ship_size=generate_ship_size(board_length, n_ships)
    ship_direction = generate_ship_direction()

    return ship_size, ship_direction
#-------------------------------------------------#


def init_ships_for_player(board_length, number_of_ships):
    #init a board for a given player

    ship_dict={}

    board = np.zeros([board_length, board_length], dtype=int)

    #For all ships, iterate ship by ship
    for i in range(len(number_of_ships)):

        #Get a random ship direction and length
            ship_size,ship_direction = generate_ship_size(board_length, number_of_ships)

        #Place ship randomly on board

            #Check for relevent cordinates to place
            cords_to_place_ship = "slice of array"

            #Try to find a sutible ship.location randomly on -possible cordinates-
                #If succesfull place
                #if not change direction

            #do this recursivly until all ships are places

        #return an object containing all *ships* to player


    return #A ship object



                                  ### Construct game ###


def prompt_to_end_loop():
    # decription
    end = 0
    while (end == 0):
        end = input("End input generation ? Y/N")

    return (1 if end == "N " else 0)


def is_number(s):
    # decription

    try:
        float(s)
        return True
    except ValueError:
        return False

def player_dict_from_user():
    # decription

    player_dict={}

    while(True):

        p_name = input("player name")
        p_type = input("player type")

        player_dict[p_name]=p_type

        if (prompt_to_end_loop()==1): break

    return player_dict


def get_params_from_user():
    # decription

    size_of_board = int(input("Input board_length"))
    number_of_ships = int(input("Input number_of_ships"))
    player_dict = player_dict_from_user()

    return player_dict,size_of_board,number_of_ships


def init_game(size_of_board, number_of_ships, player_dict):
    # decription

    game =  Game()
    size_of_board, number_of_ships, player_dict = get_params_from_user()

    game.init_board(size_of_board, number_of_ships)

    game.init_players(player_dict)

    return game


def game_menu(self):
    # decription
    ...


def turn_of_one_player(self):
    # decription
    ...



                                ### Classes ###
class ship(object):

    def __init__(self, id):
        self.id = id
        self.length
        self.direction
        self.location =[]

    def set_location(self, location_arr):
        self.location= location_arr

    def set_direction(self, direction):
        self.direction= direction

    def set_length(self, length):
        self.length= length

class Player(object):

    def __init__(self, Name):
        self.Name = Name


    def Hit(self,x,y):
        ...


class Human(Player):

    def __init__(self, name):

        self.name = name
        super().__init__(self)


class AI(Player):

    def __init__(self, name):

        self.name = name
        super().__init__(self)


class Game(object):

    def __init__(self):
        self.ship_dict = {}
        self.player_dict = {}
        self.board = []


    def still_live_players(self):
        # if player_dict empty return 0 else 1
        ...

    def make_player(self, name, kind):
        # decription

        if kind == "human":
            return Human(name)
        else:
            return AI(name)


    def add_player(self,name,kind):
        # decription
        p = self.make_player(name,kind)
        self.player_dict[name] = p

    def init_players(self, player_dict):
        # decription
        for player_name in player_dict:
            player_kind = player_dict[player_name]
            self.add_player(player_name,player_kind)

    def init_board(self, board_length, number_of_ships):
        # decription

        self.board = init_ships_for_player(board_length, number_of_ships)


    def kill_player(self):

        # If player have no more ships get player out of player loop
        ...


