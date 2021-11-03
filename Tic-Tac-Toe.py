import random

print('Welcome to tic tac toe game.')
print('Write \'exit\' to stop playing!')

grid = '___|___|___\n___|___|___\n   |   |   \n'
list_grid = list(grid)
computer_played_positions = list()
human_played_positions = list()
all_played_positions = computer_played_positions + human_played_positions
win = [[1, 5, 9], [13, 17, 21], [25, 29, 33], [1, 13, 25], [5, 17, 29], [9, 21, 33], [1, 17, 33], [9, 17, 25]]
nums_to_positions = {'1': 1, '2': 5, '3': 9, '4': 13, '5': 17, '6': 21, '7': 25, '8': 29, '9': 33}
#the variable above keeps the positions the user enters and their corresponding real position in the grid list
all_available_positions = [1, 5, 9, 13, 17, 21, 25, 29, 33]


def restart_game():
    global grid
    grid = '___|___|___\n___|___|___\n   |   |   \n'
    global list_grid
    list_grid = list(grid)
    global computer_played_positions
    computer_played_positions = list()
    global human_played_positions
    human_played_positions = list()
    global all_played_positions
    all_played_positions = computer_played_positions + human_played_positions

def check(positions):
    """checks if the human or the computer have won based on the winning positions saved in the win list"""
    count = 0
    for i in win:
        for j in i:
            if j in positions:
                count += 1
        if count == 3:
            return True
        else:
            count = 0
    return False

def change_grid(num, character):
    """changes the grid, based on the position and character played"""
    pos = nums_to_positions[num]
    list_grid[pos] = character
    if character == 'X':
        add_position(human_played_positions, pos)
        add_position(all_played_positions, pos)
            
    if character == '0':
        add_position(computer_played_positions, pos)
        add_position(all_played_positions, pos)
        

def print_grid():
    for i in list_grid:
        print(i, end='')

def add_position(list, pos):
    """adds a new played position in the list that keeps track
        of the played positions of a player, or both (depends on the given argument)""" 
    list.append(pos)


def pick_computer_position():   #pozita zgjidhet randomly
    e = list()   #pozitat e lira ku mund te luhet
    for i in all_available_positions:
        if i not in all_played_positions:
            e.append(i)
    pos = random.choice(e)
    for i in nums_to_positions:
        if nums_to_positions[i] == pos:
            pos = i
    return pos


def check_already_played_pos(pos, list):
    """checks if a position has already been played by the human or the computer,
        depending on the list given as an argument"""
    num = int(pos)
    if 1 <= num <= 9:
        num = nums_to_positions[pos]
        return num in list


while True:
    played_position = input('\nChoose a number between 1 to 9: ')
    if played_position == '':
        restart_game()
        continue
    elif played_position == 'exit':
        break
    elif played_position.isnumeric() == False:
        print('That\'s not a number. Try again!\n')
        continue
        #print(type(played_position))
    elif int(played_position) < 1 or int(played_position) > 9:
        print('The position you entered doesn\'t exist2')
        continue
    elif check_already_played_pos(played_position, human_played_positions):
        print('You have already played in that position. Choose another one!\n')
        continue
    elif check_already_played_pos(played_position, all_played_positions):
        print('That position has already been played. Choose another one!\n')
        continue
    else:
        try:
            change_grid(played_position, 'X')
            pos = pick_computer_position()
            
            if check(human_played_positions) == True:
                print_grid()
                print('You won the game!')
                played_position = input('\nPress Enter to play again or type \'exit\' to stop playing: ')
                if played_position == '':
                    restart_game()
                    continue
                if played_position == 'exit':
                    break
                
            change_grid(pos, '0')
            print_grid()
            
            if check(computer_played_positions) == True:
                print('Computer won the game!')
                played_position = input('\nPress Enter to play again or type \'exit\' to stop playing: ')
                if played_position == '':
                    restart_game()
                    continue
                if played_position == 'exit':
                    break
        except:
            print_grid()
            print('No one won!')
            played_position = input('\nPress Enter to play again or type \'exit\' to stop playing: ')
            if played_position == '':
                restart_game()
                continue
            if played_position == 'exit':
                break
        
        


