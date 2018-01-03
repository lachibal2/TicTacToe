# Tic Tac Toe
Classic Tic Tac Toe game in Python with two player functionality or a singleplayer with an AI.

## Information:
This repository was made by Lachi Balabanski. It is a python implementation of the game, tic-tac-toe. To win: get 3 of the same symbol horizontally in a row, vertically in a row, or on the diagonals. The game uses matrices from numpy to store and display the current board. The computer uses dynamic programming and memoization, which is why 'data.txt' is included in the repository.

This repository uses numpy, os, and random. os and random are built-in, but numpy is not. Be sure to pip install numpy before using.

## Use:
**two_player.py** is the two player version. The indices for the matrix is:


        1  2  3
    1 [[0  0  0 ]
    2  [0  0  x ]
    3  [0  0  0 ]]

the '_x_' is located at 2, 3

If data.txt is not found in the current working directory, the program will raise a <code>NameError</code> To resolve the error, add it to the directory.

**vs_computer.py** is the singleplayer against an easy AI version. The matrix indices are the same for the AI version as well as the two player version.

**wipe_data.py** is a function that can be executed from the terminal to remove all of the computer's memory. If the clearing of data was successful, the program will print 'Cleared Data File'

**data.txt** is a data file for the memoization part of the '_vs_computer.py_' version of the game. The current data in _data.txt_ is dummy data. Please clear the file so that it has nothing written in it, before you play the '_vs_computer.py_' version of the game. _Wipe_data.py_ was made for this purpose.

_Thank you for visiting this repo!_
