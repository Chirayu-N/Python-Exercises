# -*- coding: utf-8 -*-
"""Exercise 29 - Tic Tac Toe Full Game

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12d6XnUXplB2lKzYa7BiK5hsBtT42IXzx
"""

# Creating the board
def create_board(game):
    print('\n')
    print (' C  1    2   3 ')
    print ('R      |   |   ')
    print ('1  ' +game[0][0]+ '   | ' +game[0][1]+ ' |   ' +game[0][2] )
    print ('       |   |   ')
    print ('   ---------------')
    print ('       |   |   ')
    print ('2  ' +game[1][0]+ '   | ' +game[1][1]+ ' | ' +game[1][2] )
    print ('       |   |   ')
    print('   -----------------')
    print ('       |   |   ')
    print ('3  ' +game[2][0]+ '   | ' +game[2][1]+ ' |' +game[2][2] )
    print ('       |   |   ')
    print('\n')

# Drawing the player's choice
def place(A, who_playing):
  new_A = tuple(input(f'Where should {A} go? (row, col.) ').split(', '))
  A_row, A_col = int(new_A[0]), int(new_A[1])
  if game[A_row - 1][A_col - 1] == ' ':
    game[A_row - 1][A_col - 1] = A
    create_board(game)
    return False, True # player, opponent
  else:
    print('That spot is already taken, try again')
    return True, False # player, opponent

# Checking the board

def h_check(game, player): # Horizontal check
    for i in range(0,3):
      if game[i][0] == game[i][1] == game[i][2] == player:
        return True


def v_check(game, player): # Vertical check
    for i in range(0,3):
      if game[0][i] == game[1][i] == game[2][i] == player:
        return True


def d_check(game, player):
    if game[0][0] == game[1][1] == game[2][2] == player:
          return True
    elif game[0][2] == game[1][1] == game[2][0] == player:
          return True

def has_won(game, player):
  if h_check(game, player) or v_check(game, player) or d_check(game, player):
    return True

game = [[' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']]

X_playing = True # X goes first
O_playing = False

create_board(game)
is_playing = True
while any(' ' in sub for sub in game) and is_playing: # Only if space remains in matrix
  while X_playing and is_playing:
    X_playing, O_playing = place('X', X_playing)
    if has_won(game, 'X'):
      print('X has won')
      is_playing = False

  if any(' ' in sub for sub in game) and is_playing: # For last turn where O has no space
    while O_playing:
      O_playing, X_playing = place('O', O_playing)
      has_won(game, 'O')
      if has_won(game, 'O'):
        print('O has won')
        is_playing = False

print('Game over')