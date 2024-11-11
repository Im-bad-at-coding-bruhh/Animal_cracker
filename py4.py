from random import randint
correct_guess = randint(0,10)
players_guess = []


while True:
    guess = int(input("I'm thinking of a number from 1-10 \n"))
    
    players_guess.append(guess)

    
    if guess == correct_guess:
        print('Thats correct')
        print(f'Your guesses were {players_guess}')
        break
    elif guess < 0 or guess > 10:
        print("Out of bound bruhh")
        continue
    elif abs(correct_guess-guess) < abs(guess-players_guess[0]):
        print('Warmer')
    elif abs(correct_guess-guess) > abs(guess-players_guess[0]):
        print('Colder')
    else:
        print(f'{guess} is incorrect try again buddy')
        continue
#Ion think the warmer and colder functions work properly