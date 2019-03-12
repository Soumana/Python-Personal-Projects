import connectfour

game_state = connectfour.new_game()


def get_valid_move():
    user_response = input('Would you like to make a move or pop a piece? (Enter m or p) ').split()
    while user_response[0].lower() != 'm' and user_response[0].lower() != 'p' or len(user_response) > 1:
        print()
        print('Invalid - Enter m or p')
        print()
        user_response = input('Would you like to make a move or pop a piece? (Enter m or p). ').split()
    print()
    user_move = input('Enter a column number: ').split()
    while len(user_move) > 1 or not str(user_move[0]).isdigit() or user_move[0] not in '1234567':
        print('Invalid - Enter a number from 1 to 7')
        print()
        user_move = input('Enter a column number: ').split()

    return user_response, user_move



def rotate_game_board(board):
    result = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    new_board = []
    for r in result:
       new_board.append(r)
    return new_board


def print_game_board(board_game):
    for i in range(1, len(board_game[0]) + 1):
        print(i, end='  ')
    print()
    for sub_list in board_game:
        for item in sub_list:
            if item == '.':
                print(item, end='  ')
            elif item == 1:
                print('R', end='  ')
            elif item == 2:
                print('Y', end='  ')
        print()

def play_game(game_state):
    start = False
    while not start:

        current_game_state = game_state
        new_board = rotate_game_board(current_game_state.board)
        print_game_board(new_board)

        print()
        if current_game_state.turn == 1:
            print('Red Player Turn')
        else:
            print('Yellow Player Turn')
        print()


        try:
            user_response, user_move = get_valid_move()

            if len(user_response) == 1 and user_response[0].lower() == 'm':
                game_state = connectfour.drop(current_game_state, int(user_move[0]) - 1)
            else:
                game_state = connectfour.pop(current_game_state, int(user_move[0]) - 1)

            print()



            champ = connectfour.winner(game_state)
            if champ == 1:
                new_board = rotate_game_board(game_state.board)
                print_game_board(new_board)
                print()
                print('Red Player Won')
                start = True
            elif champ == 2:
                new_board = rotate_game_board(game_state.board)
                print_game_board(new_board)
                print()
                print('Yellow Player won')
                start = True


        except connectfour.InvalidMoveError:
            print()
            print('Invalid - Try Again')
            print()


play_game(game_state)









