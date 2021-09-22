print("Welcome to tic tac toe!")

print("""
   |   |
-----------
   |   |
-----------
   |   |
""")

starting_player = input("Choose X or O to start!\n").capitalize()

tic_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def play(player, array):
    is_winner = False

    column = int(input("Choose a column between 0 and 2\n"))
    row = int(input("Choose a row between 0 and 2\n"))

    array[column][row] = player

    print(f"""
     {array[0][0]} | {array[1][0]}  | {array[2][0]}
    -----------
     {array[0][1]} | {array[1][1]}  | {array[2][1]}
    -----------
     {array[0][2]} | {array[1][2]}  | {array[2][2]}
    """)


    for column in array:
        if column[0] == player and column[1] == player and column[2] == player:
            is_winner = True
            print(f"{player} won the game!")
            return 

    
    if (array[0][0] == player and array[1][0] == player and array[2][0] == player) or (array[0][1] == player and array[1][1] == player and array[2][1] == player) or (array[0][2] == player and array[1][2] == player and array[2][2] == player) or (array[0][0] == player and array[1][1] == player and array[2][2] == player) or (array[0][2] == player and array[1][1] == player and array[2][0] == player):
        is_winner = True
    else:
        is_winner = False
       
    
    if is_winner:
        print(f"{player} won the game!")
    else:
        if player == "X":
            player = "O"
        else:
            player = "X"
        
        print("Time for the next player!")
        play(player, array)
    
    

play(starting_player, tic_array)
