import numpy
print("Welcome to Lachi Balabanski's 2 player Tic Tac Toe game in Python")
user1 = input("Player 1, what is your name? ")
user2 = input("Player 2, what is your name? ")
user1 = str(user1)
user2 = str(user2)
board = numpy.matrix([[0,0,0],[0,0,0],[0,0,0]])
count,cond = 0,0
print(user1 + ": 1" + " \n" + user2 + ": 2")
while True:
    print(board)
    print(user1 + "'s turn ")
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
    print(user2 + "'s turn ")
    while True:
        move = input("Separate, by commas, your move coordinates ")
        move = move.split(',')
        try:
            move[0], move[1] = int(move[0]), int(move[1])
            if board[move[0] - 1,move[1] - 1] != 0:
                print("Invalid Move")
            else:
                board[move[0] - 1, move[1] - 1] = 2
                count += 1
                break
        except (ValueError, IndexError):
            print("Invalid Coordinates, try again ")
    if count == 9:
        print("Tie!")
        break
    for i in range(3):
        if board[i, 0] == 2 and board[i, 1] == 2 and board[i, 2] == 2:
            print(user2 + " Wins!")
            cond = 1
            break
        elif board[0,i] == 2 and board[1,i] == 2 and board[2,i] == 2:
            print(user2 + " Wins!")
            cond = 1
            break
    if board[0,0] == 2 and board[1,1] == 2 and board[2,2] == 2:
        print(user2 + " Wins!")
        cond = 1
    elif board[0,2] == 2 and board[1,1] == 2 and board[2,0] == 2:
        print(user2 + " Wins!")
        cond = 1
    if cond == 1:
        break
    if count == 9:
            print("Tie!")
            break
print("Thank you for playing!")
