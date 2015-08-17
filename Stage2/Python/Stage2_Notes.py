
# Problem Statement: find last occurance position of target_string in search_string
def find_last(search_string, target_string):
    search_location = 0
    while search_string.find(target_string, search_location) >= 0:
        search_location = search_string.find(target_string, search_location) + 1
    return search_location-1

# Problem Statement: http://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/
strings = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def count_letters(start, end):
    # re-assign
    if start > end:
        start = start + end
        end = start - end
        start = start -end
    # assert(end < 10000)
    sum_of_letters = 0
    for i in range(start, end+1):
        sum_of_letters += get_thousands(i) + get_hundreds(i) + get_tens(i) + get_ones(i)
    return sum_of_letters

def get_thousands(number):
    if number/1000 > 0:
        if number % 1000 > 0 and number % 1000 < 100:
            print str(number) + ' thousands :' + strings[number/1000] + ' thousand and'
            return len(strings[number/1000]) + 11
        else:
            try:
                print str(number) + ' thousands :' + strings[number/1000] + ' thousand '
                return len(strings[number/1000]) + 8
            except KeyError:
                print '-->' + str(number) + ' thousands :' + str(get_tens(number/1000)) + str(get_ones(number/1000)) + 'thousand'
                return get_tens(number/1000) + get_ones(number/1000) + 8
    else:
        return 0

def get_hundreds(number):
    if (number % 1000)/100 > 0:
        if number % 100 > 0 and number % 100 < 100:
            print str(number) + ' hundreds :' + strings[(number % 1000)/100] + ' hundred and'
            return len(strings[(number % 1000)/100]) + 10
        else:
            print str(number) + ' hundreds :' + strings[(number % 1000)/100] + ' hundred'
            return len(strings[(number % 1000)/100]) + 7
    else:
        return 0

def get_tens(number):
    if (number % 100)/10 > 1:
        print str(number) + ' tens :' + strings[(number % 100)/10 * 10]
        return len(strings[(number % 100)/10 * 10])
    else:
        return 0

def get_ones(number):
    if (number % 100) > 19 and number%10 > 0:
        print str(number) + ' ones :' + strings[number % 10]
        return len(strings[number % 10])
    elif number%100 < 20 and  number%100 > 0:
        print str(number) + ' ones :' + strings[(number % 100)]
        return len(strings[(number % 100)])
    else:
        return 0

# Problem Statement 3: Check if a matrix is a identity matrix
def matrix_check(matrix):
    if not isinstance(matrix, list):
        raise Exception("matrix is not a list")
    else:
        for row in matrix:
            if not isinstance(row, list):
                raise Exception("one of the row is not a list")

def square_check(matrix):
    matrix_check(matrix)
    for row in matrix:
        if len(row) != len(matrix):
            return False
    return len(matrix)

def identity_check(matrix):
    order = square_check(matrix)
    if order:
        for row in range(order):
            for column in range(order):
                if row == column:
                    if matrix[row][column] != 1:
                        return False
                else:
                    if matrix[row][column] != 0:
                        return False
    else:
        return False
    return True


# Problem Statement #4: Create a list of random 20 numbers between 0 and 10:
def get_random_list():
    l = []
    import random
    for n in range(20):
        l.append(random.randint(0,10))
    return l

# Problem Statement #5: https://projecteuler.net/problem=1
def get_sum_multiples(range_of_numbers, list_of_multiples, all=False):
    sum = 0
    length = len(list_of_multiples)
    for n in range(range_of_numbers):
        for m in list_of_multiples:
            if n % m == 0 and isinstance(n/m, int):
                if not all:
                    sum += n
                    break
                elif list_of_multiples.index(m) == length - 1:
                    sum = sum + n
            elif all:
                break
    return sum

# Problem Statement #6: Build a tic-tac-toe game
positions = { "tl": " ", "tc": " ", "tr": " ",
"cl": " ", "c": " ", "cr": " ",
"bl": " ", "bc": " ", "br": " "}
def display_board():
    print '''
    -------------
    | {tl} | {tc} | {tr} |
    -------------
    | {cl} | {c} | {cr} |
    -------------
    | {bl} | {bc} | {br} |
    -------------
    '''.format(**positions)

def start_play_game():
    state_of_game = 0 #Game not started/not in progress
    current_player = "X"
    while True:
        if state_of_game == 0:
            user_choice = raw_input('''
1. Start a new game
2. Quit
Choose an option:''')
        if user_choice == "1" and state_of_game == 0:
            state_of_game = 1
            for position in positions:
                positions[position] = " "
            display_board()
        elif state_of_game == 1:
            print "Your Legal moves are:"
            legal_moves = []
            for position in positions:
                if positions[position] == " ":
                    legal_moves.append(position)
                    print position
            print "abort"
            move_choice = raw_input('''
choose a move from above legal moves [Player: {cp}]:'''.format(cp = current_player))
            if move_choice != "abort" and move_choice in legal_moves:
                positions[move_choice] = current_player
                current_player = "O" if current_player == "X" else "X"
                display_board()
                state_of_game = check_for_win()
            elif move_choice == "abort":
                print "Have a Great day!! Good Bye"
                break
            else:
                print "Not a Legal move, try again"
        elif user_choice == "2":
            print "Have a Great day!! Good Bye"
            break
        else:
            print "Illegal option chosen, Try again :)"

def check_for_win():
    win_list = [
    positions["tl"] + positions["tc"] + positions["tr"],
    positions["cl"] + positions["c"] + positions["cr"],
    positions["bl"] + positions["bc"] + positions["br"],
    positions["tl"] + positions["cl"] + positions["bl"],
    positions["tr"] + positions["cr"] + positions["br"],
    positions["tc"] + positions["c"] + positions["bc"],
    positions["tl"] + positions["c"] + positions["br"],
    positions["tr"] + positions["c"] + positions["bl"]
    ]

    if "XXX" in win_list:
        print "Player X is winner, Do you want to start a new game?"
        return 0
    elif "OOO" in win_list:
        print "Player O is winner, Do you want to start a new game?"
        return 0
    elif " " not in positions.values():
        print "Draw Game, Do you want to start a new game?"
        return 0
    else:
        print "Next Turn please :) "
        return 1

'''Tests'''
# print count_letters(119, 121)
# print '*' * 10
# print count_letters(99,101)
# print '*' * 10
# print count_letters(109,111)
# print '*' * 10
# print count_letters(9,11)
# print '*' * 10
# print count_letters(19,21)
# print '*' * 10
# print count_letters(899,901)
# print '*' * 10
# print count_letters(88,91)
# print '*' * 10
# print count_letters(1,1000)
# print count_letters(21201,21201)

# print identity_check(
#   [[1,0,0],
#   [0,1,0],
#   [0,0,1],
#   [0,0,0]])
# print identity_check([[1,0],0,1])

# print get_random_list()

# print get_sum_multiples(1000, [3,5])

start_play_game()