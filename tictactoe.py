import pyfiglet

def show():
    for row in game_board:
        for cell in row :
            print(cell," ", end=" ")
        print()

title = pyfiglet.figlet_format("tic tac toe", font="slant")
print(title)

def check_game():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O" :
        print("player2 : you win!!!")
        return 1
    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X" :
        print("player1 : you win!!!")
        return 1
    if game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O" :
        print("player2 : you win!!!")   
        return 1
    if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-" :
        print("drow!!!")
        return 2

game_board = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]
show()

while True:
    #player1
    print("player1")
    while True:
        row = int(input("enter row : "))
        col = int(input("enter col : "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-" :
                game_board[row][col] = "X"
                show()
                break
            else :
                print("enter row/col again : ")
        else:
            print("enter 0 <= row/col <= 2")
    if check_game() == 1 :
        break
    elif check_game() == 2 :
        continue

    #player2
    print("player2")
    while True:
        row = int(input("enter row : "))
        col = int(input("enter col : "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-" :
                    game_board[row][col] = "O"
                    show()
                    break
            else :
                print("enter row/col again : ")
        else :
            print("enter 0 <= row/col <= 2")
    if check_game() == 1 :
        break
    elif check_game() == 2 :
        continue
