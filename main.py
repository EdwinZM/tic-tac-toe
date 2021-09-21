print("Welcome to tic tac toe!")

print("""
   |   |
-----------
   |   |
-----------
   |   |
""")

starting_player = input("Choose X or O to start!\n")

column = int(input("Choose a column between 0 and 2\n"))
row = int(input("Choose a row between 0 and 2\n"))

tic_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def play(col, row, player, array):
    is_winner = False

    array[col][row] = player

    print(f"""
     {array[0][0]} | {array[1][0]}  | {array[2][0]}
    -----------
     {array[0][1]} | {array[1][1]}  | {array[2][1]}
    -----------
     {array[0][2]} | {array[1][2]}  | {array[2][2]}
    """)

    print("Time for the next player!")

    if array[0][0] == player and array[0][1] == player and array[0][2] == player:
        is_winner = True

    if player == "X":
        player = "O"
    else:
        player = "X"
    
    

play(column, row, starting_player, tic_array)
