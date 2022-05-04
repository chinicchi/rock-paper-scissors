import random

lst = ['Rock', 'Paper', 'Scissors']

def comp_choice():
    comp = random.choice(lst)
    return comp

def player_choice():
    player = 'wrong'
    while player not in ['r', 'p', 's']:
        player = input('Enter r (rock), p (paper), or s (scissors) : ')
        if player not in ['r', 'p', 's']:
            print("I don't understand. Please make sure enter r, p, or s.")
    return player

def start_game():
    start = input('Ready to play rock-paper-scissors game? y or n? ')
    while start not in ['y', 'n']:
        start = input("I don't understand. Please enter y or n : ")
    if start == 'y':
        return True
    else:
        print("I don't want to play")
        return False


def game_on_choice():
    choice = 'wrong'
    while choice not in ['y','n']:
        choice = input('Want to play again? y or n? ')
        if choice not in ['y', 'n']:
            print("I don't understand. Please make sure enter y or n.")
    if choice == 'y':
        return True
    else:
        print('You done playing!')
        return False

game_on = start_game()

while game_on:
    comp = comp_choice()
    player = player_choice()

    if comp == 'Rock':
        if player == 'r':
            print(f"{comp} vs Rock. It's a  draw!")
        elif player == 'p':
            print(f'{comp} vs Paper. Player win!')
        elif player == 's':
            print('Rock vs Scissors. Computer win!')
    elif comp == 'Paper':
        if player == 'r':
            print(f'{comp} vs Rock. Computer win!')
        elif player == 'p':
            print(f"{comp} vs Paper. It's a  draw!")
        elif player == 's':
            print(f'{comp} vs Scissors. Player win!')
    elif comp == 'Scissors':
        if player == 'r':
            print(f'{comp} vs Rock. Player win!')
        elif player == 'p':
            print(f'{comp} vs Paper. Computer win!')
        elif player == 's':
            print(f"{comp} vs Scissors. It's a  draw!")

    game_on = game_on_choice()


