def display_board(board):
    
    print('       |       |      ')
    print(f'  {test_board[1]}    |  {test_board[2]}    |  {test_board[3]}  ')
    print('       |       |      ')
    print('____________________  ')  
    print('       |       |      ')
    print(f'  {test_board[4]}    |  {test_board[5]}    |  {test_board[6]}  ')
    print('       |       |      ')
    print('____________________  ')
    print('       |       |      ')
    print(f'  {test_board[7]}    |  {test_board[8]}    |  {test_board[9]}  ')
    print('       |       |      ')

def player_input():
    
  pi = ''
        
  while pi not in ['X','O',]:
    pi = input('Assign marker X or O ').capitalize()
    print('\n' * 100)
        
  if 'X' not in pi:
    return (pi,'X')
  if 'O' not in pi:
    return (pi,'O')

def place_marker(board, marker, position):
    
  while position not in range(1,10):
        
    print(f'Position {position} is not valid')
    break
        
  if position in range(1,10):
        
    board[position] = marker

def win_check(board, mark):
    
    
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    return False

from random import randint

def choose_first():
    
    choosen =[randint(2,4)]
    
    for num in choosen:
        if num % 2 == 0:
            return 'Player 1'
        else:
            return 'Player 2'
        
def space_check(board, position):
    
    return board[position]  == ' '

def full_board_check(board):
    
     if (test_board[1] != ' ' and test_board[2] != ' ' and test_board[3] != ' ' and test_board[4] != ' ' and test_board[5] != ' ' and test_board[6] != ' ' and test_board[7] != ' ' and test_board[8] != ' ' and test_board[9] != ' '):
        return True
     return False

def player_choice(board):
    
    pc = ""
    
    while (pc.isdigit() == False or int(pc) not in range(1,10)):
        
        pc = input('Enter a number in range 1 - 9 ')
        
        if space_check(board,int(pc)) == True:
            return int(pc)
    print(f"{pc} is already taken")

def replay():
    
    rp = ''
    
    while rp.capitalize() not in ['Y','N']:
        
        rp = input('Would you like to play again Y or N ')
  
    if rp == 'Y':
        return True
    if rp == 'N':
        return False
    
print('Welcome to Tic Tac Toe!')

while True:
    
    test_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No. ')
    print('\n' * 100)
    
    if play_game.lower()[0] == 'y':
        game_on = True
    if play_game.lower()[0] == 'n':
        game_on = False

    while game_on:
        if turn == 'Player 1':
            
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1_marker, position)
            print('\n' * 100)
            if win_check(test_board, player1_marker):
                display_board(test_board)
                print('Congratulations! You have won the game!')
                game_on = False
            
            elif full_board_check(test_board):
                display_board(test_board)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 2'

        else:
            
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2_marker, position)
            print('\n' * 100)
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print('Player 2 has won!')
                game_on = False

            elif full_board_check(test_board):
                display_board(test_board)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 1'

    if not replay():
        break