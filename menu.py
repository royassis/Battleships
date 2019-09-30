import sys
import numpy as np

#Switch case implementation for user interface

#############
def exit_game():
    sys.exit(0)

#############
def game_menu():
    print("game_menu:\n"
          "0 To exit\n"
          "1 To list help\n"
          "2 Nships\n"
          "3 Board\n"
          "4 shipDict\n"
          "5 HitBoard\n")

#############
def prn_Nships(player):
    print(player.Nships)

#############
def prn_shipDict(player):
    for i in player.shipDict:
        print("ship",i,"shipsize:",player.shipDict[i])
    print("\n")

#############
def prettyBoardHeader(player):
    length= len(player.Board[0])
    s = "  ".join([str(i+1) for i in range(length)])
    print("\t",s,"\n")

def prettyBoardIndex(board):
    for i,j in enumerate(board):
        print(i+1,"\t", "  ".join(map(str,j)))

def prn_Board(player):

    prettyBoardHeader(player)
    board = np.array(player.Board[0]).astype(int)
    prettyBoardIndex(board)
    print("\n")


def prn_HitBoard(player):

    #print header
    prettyBoardHeader(player)

    #build empty new array
    length = len(player.Board[0].ravel())
    arr = np.zeros(length, dtype=int)

    #fill with 2 or 1
    for i,(j,k) in enumerate(zip(player.Board[0].ravel(),player.Board[1].ravel())):

        if j != 0 and k == 1:
            arr[i]= "2"
        if j == 0 and k == 1:
            arr[i]= "1"

    #print new arr
    side = player.Board[0].shape[0]
    newarr= arr.reshape(side,side)
    prettyBoardIndex(newarr)

    print("\n")


#############
interface_options = {"exit": exit_game(),
                     "help": game_menu(),
                     "prn_Nships": prn_Nships(),
                     "prn_Board": prn_Board(),
                     "prn_shipDict": prn_shipDict(),
                     "prn_HitBoard": prn_HitBoard(),
                     }

