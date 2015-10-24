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

start_play_game()