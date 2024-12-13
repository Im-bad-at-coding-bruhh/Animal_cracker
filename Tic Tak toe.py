game_dict = { 1 : '', 2 : '',3 : '', 4 : '',5 : '', 6 : '',7 : '', 8 : '', 9 : ''}
f = []

def display_game(game_dict):
    print('       |       |      ')
    print(f'  {game_dict[1]}    |  {game_dict[2]}    |  {game_dict[3]}  ')
    print('       |       |      ')
    print('____________________  ')  
    print('       |       |      ')
    print(f'  {game_dict[4]}    |  {game_dict[5]}    |  {game_dict[6]}  ')
    print('       |       |      ')
    print('____________________  ')
    print('       |       |      ')
    print(f'  {game_dict[7]}    |  {game_dict[8]}    |  {game_dict[9]}  ')
    print('       |       |      ')

def user_position():

    gg = ''
    
    while gg.isdigit() == False or int(gg) not in range(1,10):
        
        gg = input('Input value between 1-9 ---- ')
        
              
    return int(gg)   
   
def check_user():
    
    nnn = ''
    
    while nnn not in ['X','O','x','o']:
        
        nnn = input('Would you like to be X or O ---- ')
    return nnn.capitalize()

def repeated(x):
    
    while x not in f:

        f.append(x)
        return x
    return user_position()

def update_value_for_X_or_O(hhh,mmm):
    
    for i in game_dict:
        if i == hhh:
            game_dict[i] = mmm           
    return game_dict

def is_win():
    
    
    if game_dict[1] == 'X' and game_dict[2] == 'X' and game_dict[3] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[1] == 'O' and game_dict[2] == 'O' and game_dict[3] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[4] == 'X' and game_dict[5] == 'X' and game_dict[6] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[4] == 'O' and game_dict[5] == 'O' and game_dict[6] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[7] == 'X' and game_dict[8] == 'X' and game_dict[9] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[7] == 'O' and game_dict[8] == 'O' and game_dict[9] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[1] == 'X' and game_dict[4] == 'X' and game_dict[7] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[1] == 'O' and game_dict[4] == 'O' and game_dict[7] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[2] == 'X' and game_dict[5] == 'X' and game_dict[8] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[2] == 'O' and game_dict[5] == 'O' and game_dict[8] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[3] == 'X' and game_dict[6] == 'X' and game_dict[9] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[3] == 'O' and game_dict[6] == 'O' and game_dict[9] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[1] == 'X' and game_dict[5] == 'X' and game_dict[9] == 'X':
        print("Congratulations 'X' wins")
        return False
    elif game_dict[1] == 'O' and game_dict[5] == 'O' and game_dict[9] == 'O':
        print("Congratulations 'O' wins ")
        return False
    elif game_dict[3] == 'X' and game_dict[5] == 'X' and game_dict[7] == 'X':
        print("Congratulations 'X' wins")
        return False
    if game_dict[3] == 'O' and game_dict[5] == 'O' and game_dict[7] == 'O':
        print("Congratulations 'O' wins ")
        return False
    
    return True

def is_draw():
    
    if (game_dict[1] != '' and game_dict[2] != '' and game_dict[3] != '' and game_dict[4] != '' and game_dict[5] != '' and game_dict[6] != '' and game_dict[7] != '' and game_dict[8] != '' and game_dict[9] != ''):
        print("Stand down it's a draw")
        return False
    else:
        return True
    

gameon = is_win() 
gamedraw = is_draw()

while gameon and gamedraw:
    
    display_game(game_dict)
    c = repeated(user_position())
    print('\n' * 100)
    uwu = update_value_for_X_or_O(c,check_user())
    display_game(uwu)
    print('\n' * 100)
    gameon = is_win()
    gamedraw = is_draw()