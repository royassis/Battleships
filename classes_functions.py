import numpy as np
from scipy.stats import  norm
from collections import defaultdict


                                ### Construct board ###


def generate_ship_size(board_length, n_ships):
    # Returns ship size when constructing board

    board_size = board_length**2
    avg_ship_size = board_size/(n_ships*3)
    ship_size = norm.ppf(np.random.random(1), loc=avg_ship_size, scale=2).astype(int)[0]

    return ship_size


def relevent_cords(board_length, ship_size, board_to_check, upper_xy):
    # Returns a dictionary with the keys as suitable row numbers and values as suitable elemnts in each row

    d = defaultdict(list)
    for i in range(board_length):

        for j in range(upper_xy + 1):

            counter = 0
            for k in range(ship_size):

                if board_to_check[i, j + k] == 0:
                    counter = 1 + counter
                else:
                    counter = 0
            if counter >= ship_size:
                d[i].append(j)
    return d


def set_ship(dict, board_to_check, ship_size, ship_counter):
    # Returnes a board with the ship numbers

    random_i = np.random.choice(list(dict.keys()))
    random_j = np.random.choice(dict[random_i])

    for k in range(ship_size):
        board_to_check[random_i, random_j + k] = ship_counter


def check__if_full(board):

    length = len(board[0].ravel())
    if np.count_nonzero(board[0]) == length:
        return 1
    return 0


def init_board(board_size, number_of_ships):
    # Joins all the above functions in order to place a new ship.returns the new board with the places ship and a list of ships as a dict
    ship_dict={}

    board = np.zeros([2, board_size, board_size], dtype=int)
    ship_counter = 0

    #For all ships, iterate ship by ship
    while ship_counter<number_of_ships:

        #Get ship size and direction
        ship_size, direction = generate_ship_size(board_size)

        upper_xy = board_size - ship_size

        #check if ship placment on board is ok
        board_to_check = board[0] if direction == 0 else board[0].T

        #get cords to place ship
        dict = relevent_cords(board_size, ship_size, board_to_check, upper_xy)

        #if cords are not good try again with same ship
        if not(dict):
            continue

        #if cords are good place ship
        set_ship(dict, board_to_check, ship_size, ship_counter + 1)

        # Input ship and ship size into ship dictionary
        ship_dict[ship_counter + 1] = ship_size

        ship_counter = ship_counter + 1

    return ship_dict



                                  ### Construct game ###


def is_number(s):
    # decription

    try:
        float(s)
        return True
    except ValueError:
        return False


def get_params_from_user():
    # decription

    input_ok=0
    while (input_ok == 0 ):

        size_of_board = input("Input board_length")
        number_of_ships = input("Input number_of_ships")

        if  is_number(size_of_board) == False or \
            is_number(number_of_ships) == False:
            print("wrong input")

            continue

        else:
            size_of_board = int(size_of_board)
            number_of_ships = int(number_of_ships)

        if (size_of_board == 0 or number_of_ships == 0):
            print("Please pick a resonable size")
            continue

        if (size_of_board < number_of_ships ):
            print("board too small")
            continue

        input_ok = 1


    return size_of_board,number_of_ships


def init_game(size_of_board, number_of_ships, player_dict):
    # decription

    game =  Game()
    game.init_board(size_of_board, number_of_ships)

    for name, kind in player_dict.keys:
        game.make_player(name, kind)

    return game


def game_menu(self):
    # decription
    ...


def turn_of_one_player(self):
    # decription
    ...



                                ### Classes ###


class Player(object):

    def __init__(self, Name):
        self.Name = Name


    def Hit(self,x,y):
        ...


class Human(Player):

    def __init__(self, name):

        self.name = name
        super().__init__(self, name)


class AI(Player):

    def __init__(self, name):

        self.name = name
        super().__init__(self, name)


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

        if kind == 1:
            return Human(name)
        else:
            return AI


    def add_player(self,name,kind):
        # decription

        p = self.make_player(name,kind)
        self.player_dict[name] = p


    def init_board(self, board_length, number_of_ships):
        # decription

        self.board = init_board(board_length, number_of_ships)


    def kill_player(self):

        # If player have no more ships get player out of player loop
        ...




