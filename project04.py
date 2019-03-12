import othelloGameLogic

def get_row():
    rows = input('How many rows? ').split()
    while len(rows) != 1 or not rows[0].isdigit() or int(rows[0]) < 4:
        print('Invalid, enter a number from 4 and up')
        rows = input('How many rows? ').split()
    return int(rows[0])


def get_col():
    col = input('How many columns? ').split()
    while len(col) != 1 or not col[0].isdigit() or int(col[0]) < 4:
        print('Invalid, enter a number from 4 and up')
        col = input('How many columns? ').split()
    return int(col[0])

def get_color():
    color = input('Which color will start? ').split()
    while len(color) != 1 or not color[0].isalpha() or color[0].lower() != 'b' and color[0].lower() != 'w':
        print('Invalid, enter B or W')
        color = input('Which color will start? ').split()
    return color[0]


def get_move(total_rows, total_cols):
    while True:
        move = input('Enter row and column: ').split()
        if len(move) == 2:
            if move[0].isdigit() and move[1].isdigit():
                if int(move[0]) >= 1 and int(move[0]) <= total_rows and int(move[1]) >= 1 and int(move[1]) <= total_cols:
                    return int(move[0]) - 1, int(move[1]) - 1

def how_to_win():
    while True:
        rule = input('Enter < or > ').split()
        if len(rule) == 1:
            if rule[0] == '<' or rule[0] == '>':
                return rule[0]

def begin_game():
    total_rows = get_row()
    total_col = get_col()
    color = get_color()
    rules = how_to_win()
    othello = othelloGameLogic.GameBoard(total_rows, total_col, color)
    othello.create_board()
    print()

    turn = othello.current_player_turn()


    while True:

        black_score, white_score = othello.score()
        print('B: ' + str(black_score) + ' W: ' + str(white_score) + "\n")

        othello.print_game_board()
        print()

        print('Turn: ' + turn + "\n")


        row, col = get_move(total_rows, total_col)
        othello.make_move(row, col, turn)
        print()
        print()

        turn = othello.next_player_turn(turn)

        if not othello.check_valid_moves(turn):
            turn = othello.next_player_turn(turn)
            if not othello.check_valid_moves(turn):
                winner = othello.winner(rules, black_score, white_score)
                if winner == 'Tie':
                    print('Game over - ' + winner)
                else:
                    print('Game Over - ' + winner + ' won')

                return


if __name__ == '__main__':
    begin_game()