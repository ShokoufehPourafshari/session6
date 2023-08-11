from pyfiglet import Figlet

def show():
    for row in game_bord:
        for cel in row:
            print(cel, end=" ")
        print()

def check_game1():
    
    if game_bord[0][0] == "X" and game_bord[0][1] == "X" and game_bord[0][2] == "X" :
        print("player1 won")
        return True
    
    if game_bord[0][0] == "X" and game_bord[1][1] == "X" and game_bord[2][2] == "X" :
        print("player1 won")
        return True
    
    if game_bord[0][1] == "X" and game_bord[1][1] == "X" and game_bord[2][1] == "X" :
        print("player1 won")
        return True
    
    if game_bord[0][2] == "X" and game_bord[1][2] == "X" and game_bord[2][2] == "X" :
        print("player1 won")
        return True
    
    if game_bord[1][0] == "X" and game_bord[1][1] == "X" and game_bord[1][2] == "X" :
        print("player1 won")
        return True
    
    if game_bord[2][0] == "X" and game_bord[2][1] == "X" and game_bord[2][2] == "X" :
        print("player1 won")
        return True
    
    if game_bord[0][1] == "X" and game_bord[1][1] == "X" and game_bord[2][0] == "X" :
        print("player1 won")
        return True
    
    if game_bord[0][0] == "X" and game_bord[1][0] == "X" and game_bord[2][0] == "X" :
        print("player1 won")
        return True
    return False

def check_game2():
    
    if game_bord[0][0] == "O" and game_bord[0][1] == "O" and game_bord[0][2] == "O" :
        print("player2 won")
        return True
    
    if game_bord[0][0] == "O" and game_bord[1][1] == "O" and game_bord[2][2] == "O" :
        print("player2 won")
        return True
    
    if game_bord[0][1] == "O" and game_bord[1][1] == "O" and game_bord[2][1] == "O" :
        print("player2 won")
        return True
    
    if game_bord[0][2] == "O" and game_bord[1][2] == "O" and game_bord[2][2] == "O" :
        print("player2 won")
        return True
    
    if game_bord[1][0] == "O" and game_bord[1][1] == "O" and game_bord[1][2] == "O" :
        print("player2 won")
        return True
    
    if game_bord[2][0] == "O" and game_bord[2][1] == "O" and game_bord[2][2] == "O" :
        print("player2 won")
        return True
    
    if game_bord[0][1] == "O" and game_bord[1][1] == "O" and game_bord[2][0] == "O" :
        print("player2 won")
        return True
    
    if game_bord[0][0] == "O" and game_bord[1][0] == "O" and game_bord[2][0] == "O" :
        print("player2 won")
        return True
    return False

f = Figlet(font='slant')
print(f.renderText('Tic Tac Toe'))

game_bord = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]
show()
i = 0
while True:
    print("player1")
    row = int(input("Enter row:"))
    col = int(input("Enter col:"))
    if 0<= row <= 2 and 0<= col<= 2:
        if game_bord[row][col] == "-":
            game_bord[row][col]= "X"
            show()
            if check_game1():
                break
            i += 1
        else:
            print("choose another one: ")
    if i == 9:
        print("End")
        break

    print("player2")   
    while True:
        row = int(input("Enter row:"))
        col = int(input("Enter col:"))
        if 0<= row <= 2 and 0<= col<= 2:
            if game_bord[row][col] == "-":
                game_bord[row][col]= "O"
            show()
            if check_game2():
                break
            i += 1
        else:     
            print("chose another one: ")
        
        if i == 9:
            print("End")
            break