import numpy
import os
import random
def writeToFile(boardPos, des, filename='data.txt'):
    if 'data.txt' in os.listdir():
        des = str(des)
        fi = open(filename, 'a')
        boardPos = str(boardPos).replace('\n', ',')
        fi.write(boardPos + ':' + str(des) + ' \n')
        fi.close()
    else:
        raise NameError("Missing File Name: 'data.txt'")
def loadPositions(filename='data.txt'):
    try:
        if 'data.txt' in os.listdir():
            my_dict = {}
            fi = open(filename, 'r')
            for i in fi:
                current = i.replace('\n', '')
                current = current.split(':')
                my_dict[current[0]] = current[1]
            fi.close()
            return my_dict
        else:
            raise NameError('Missing File Name: data.txt')
    except IndexError:
        return {'a':1}
def getListCopy(board):
    master = []
    for i in range(0,3):
        master.append([board[0,i], board[1,i], board[2,i]])
    for i in range(len(master)):
        old = str(master[i])
        new = old.replace(',','')
        master[i] = new
    return master
def isWinning(board):
    for i in range(3):
        if board[i, 0] == 1 and board[i, 1] == 1 and board[i, 2] == 1:
            return 1
        elif board[0,i] == 1 and board[1,i] == 1 and board[2,i] == 1:
            return 1
    if board[0,0] == 1 and board[1,1] == 1 and board[2,2] == 1:
        return 1
    elif board[0,2] == 1 and board[1,1] == 1 and board[2,0] == 1:
        return 1
    for i in range(3):
        if board[i, 0] == 2 and board[i, 1] == 2 and board[i, 2] == 2:
            return 2
        elif board[0,i] == 2 and board[1,i] == 2 and board[2,i] == 2:
            return 2
    if board[0,0] == 2 and board[1,1] == 2 and board[2,2] == 2:
        return 2
    elif board[0,2] == 2 and board[1,1] == 2 and board[2,0] == 2:
        return 2
    return 0
def getBoardCopy(board):
    #did not realize matricies had a .copy() method until i called this function
    #in the code, so I decided to change it like this:
    board_c = board.copy()
    return board_c
def zeros(board):
    res = []
    for i in range(3):
        if board[i,0] == 0:
            res.append([i,0])
        if board[i,1] == 0:
            res.append([i,1])
        if board[i,2] == 0:
            res.append([i,2])
    return res
def computer_main(board):
    #Algorithm efficency of O(n)---
    boardZero = zeros(board)
    for j in boardZero:
        board_copy = getBoardCopy(board)
        board_copy[j[0],j[1]] = 2
        temp = isWinning(board_copy)
        if temp == 2:
            currentMove = j
            b1 = str(list(getListCopy(board)))
            b1.replace(' \n', ',')
            writeToFile(b1, j)
            return currentMove
    for j in boardZero:
        board_copy = getBoardCopy(board)
        board_copy[j[0],j[1]] = 1
        temp = isWinning(board_copy)
        if temp == 1:
            currentMove = j
            b1 = str(list(getListCopy(board)))
            b1.replace(' \n', ',')
            writeToFile(b1, j)
            return currentMove
    if board[1,1] == 0:
        currentMove = [1,1]
        b1 = str(list(getListCopy(board)))
        b1.replace(' \n', ',')
        writeToFile(b1, [1,1])
        return currentMove
    else:
        currentMove = boardZero[random.randint(0,len(boardZero) - 1)]
        b1 = str(list(getListCopy(board)))
        b1.replace(' \n', '')
        print("WILDCARD")
        writeToFile(b1, j)
        return currentMove
#Game Begins ---
print("Welcome to Lachi Balabanski's VS. Computer Tic Tac Toe Game in Python")
user1 = input("Player 1, what is your name? ")
user1 = str(user1).capitalize()
board = numpy.matrix([[0,0,0],[0,0,0],[0,0,0]])
count,cond = 0,0
prev_moves = loadPositions()
print(user1 + ": 1" + " \n" + "Computer: 2")
print(board)
while True:
    print(user1 + "'s turn: ")
    while True:
        move = input("Separate, by commas, your move coordinates ")
        move = move.split(',')
        try:
            move[0], move[1] = int(move[0]), int(move[1])
            if board[move[0] - 1,move[1] - 1] != 0:
                print("Invalid Move")
            else:
                board[move[0] - 1, move[1] - 1] = 1
                print(board)
                count += 1
                break
        except (ValueError, IndexError):
            print("Invalid Coordinates, try again ")
    if count == 9:
        print("Tie!")
        break
    for i in range(3):
        if board[i, 0] == 1 and board[i, 1] == 1 and board[i, 2] == 1:
            print(user1 + " Wins!")
            cond = 1
            break
        elif board[0,i] == 1 and board[1,i] == 1 and board[2,i] == 1:
            print(user1 + " Wins!")
            cond = 1
            break
    if board[0,0] == 1 and board[1,1] == 1 and board[2,2] == 1:
        print(user1 + " Wins!")
        cond = 1
    elif board[0,2] == 1 and board[1,1] == 1 and board[2,0] == 1:
        print(user1 + " Wins!")
        cond = 1
    if cond == 1:
        break
    #COMPUTER CODE:
    print("Computer's turn: ")
    try:
        b1 = str(list(getListCopy(board)))
        b1.replace(' \n', ',')
        currentMove = prev_moves[b1]
        currentMove = currentMove.replace('[', '')
        currentMove = currentMove.replace(']', '')
        currentMove = currentMove.split(',')
        currentMove[0], currentMove[1] = int(currentMove[0]), int(currentMove[1])
        print("Memoization achieved!")
    except KeyError:
        currentMove = computer_main(board)
    board[currentMove[0], currentMove[1]] = 2       
    print(board)
    count += 1
    if count == 9:
        print("Tie!")
        break
    for i in range(3):
        if board[i, 0] == 2 and board[i, 1] == 2 and board[i, 2] == 2:
            print("Computer Wins!")
            cond = 1
            break
        elif board[0,i] == 2 and board[1,i] == 2 and board[2,i] == 2:
            print("Computer Wins!")
            cond = 1
            break
    if board[0,0] == 2 and board[1,1] == 2 and board[2,2] == 2:
        print("Computer Wins!")
        cond = 1
    elif board[0,2] == 2 and board[1,1] == 2 and board[2,0] == 2:
        print("Computer Wins!")
        cond = 1
    if cond == 1:
        break
    if count == 9:
        print("Tie!")
        break
print("Thank you for playing!")
