my_matrix = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]
def pretty_display(current_matrix) :
    for i in range(len(current_matrix)) :
        print(current_matrix[i])

def check_lines(current_matrix) :
    is_there_winner = False
    for i in range(len(current_matrix)) :
        current_line = my_matrix[i]
        if (current_line[0] == current_line[1] 
            and current_line[0] == current_line[2] 
            and current_line[0] != "-" ) :
            
            is_there_winner = True

    return is_there_winner



player_turn = 0
game_over = False

while not game_over :
    picked_line = int(input("Choisi ta ligne : "))
    picked_column = int(input("Choisi ta colone : "))

    my_matrix[picked_line][picked_column] = "o" if player_turn else "x"
    pretty_display(my_matrix)
    player_turn = 1 if player_turn == 0 else 0
    if (check_lines(my_matrix) == True) :
        game_over = True
print("JEU SET ET MATCH, IL Y A UN GAGNANT : (Je sais pas qui pour le moment...)")
