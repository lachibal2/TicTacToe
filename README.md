# TicTacToe
Tic Tac Toe game in Python\

## Information:
This repository was made by Lachi Balabanski. It is a python implementation of the game, tic-tac-toe. To win: get 3 of the same symbol horizontally in a row, vertically in a row, or on the diagonals. The game uses matricies from numpy to store and display the current board. The computer uses dynamic programming and memoization, which is why 'data.txt' is included in the repository.

## Use:
two_player.py is the two player version. The indices for the matrix is:
   
    1  2  3
1 [[0  0  0 ]

2  [0  0  x ]

3  [0  0  0 ]]

the 'x' is located at 2, 3

vs_computer.py is the singleplayer against an easy AI version. The matrix indices are the same for the AI version as well as the two player version.

wipe_data.py is a function that can be executed from the terminal to remove all of the computer's memory. If the clearing of data was successful, the program will print 'Cleared Data File'. Example:

<code>$python wipe_data.py
Cleared Data File
</code>

Thank you for visiting this repo!
