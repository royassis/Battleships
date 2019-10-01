# Battleships

### Description
Computer implementation of the old Battleship boardgame  
The goal is to make a game with N virtual and human users  
and to make a trainable virtual users using machine learning

### Planing
The project will include the __actual game__ (which is the hard part)  
and the ___machine learning__ part 
  
##### Game
The structre of the planning the game as follows: 

1. Recive parametes from the user about the:
   1. Number of players
   2. Length of board (the board is a squar)
   
   * Check the paramets
2. Initiate the __Game class__:
   1. Initiate the _players_
   2. Initiate the _board_ - this will include a __recursive__  
   function in order to place  all the ships
   3. The placing of the ships is yet not  
   decided - Player objects vs. Game object
   
3. Initiate the __Game round__ and define the rules  
and how each player _attack_ another  
how players can view their board  
and the diff between human and virtual players

##### ML
The structre of the planning the ML as follows: 

The outcome of each decision, good or bad, will be saved to file.  
with the board data at that time, the position on the board,  
and maybe also the actual time and date

Problems:  

The board array will have to be normalized in order to fit a model  
this will be the hard part.
The position of the hit on the board will also  
need to be normalized in condition to the size of the board


