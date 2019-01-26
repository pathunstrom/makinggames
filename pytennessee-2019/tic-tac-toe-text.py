import random
from itertools import chain
from typing import Tuple
from typing import NamedTuple
NAUGHT = "O"
CROSS = "X"


class Player(NamedTuple):
    symbol: str
    is_human: bool


def check_horizontal(first, board):
    if board[first] is None:
        return False
    return all(board[first] == space for space in  board[first:first + 3])


def check_vertical(first, board):
    if board[first] is None:
        return False
    return all(board[first] == space for space in board[first:first + 7:3])


def check_diagonal(first, board):
    if board[first] is None:
        return False
    if first == 0:
        return all(board[first] == space for space in board[::4])
    elif first == 2:
        return all(board[first] == space for space in board[2:7:2])


def game_won(board) -> bool:

    return any(
        chain(
            map(lambda x: check_horizontal(x, board), [0, 3, 6]),
            map(lambda x: check_vertical(x, board), [0, 1, 2]),
            map(lambda x: check_diagonal(x, board), [0, 2])
        )
    )


def get_random_space(board):
    return random.choice(list(i for i, v in enumerate(board) if v is None))


def get_user_input():
    output = None
    while output is None:
        value = input("Please choose a square\n")
        try:
            x, y = value.split(",")
            x = ['a', 'b', 'c'].index(x)
            y = [1, 2, 3].index(int(y))
            output = x + (y * 3)
        except ValueError:
            print("Input should be look like 'a, 1'")
            print("X coordinate should be a letter: a, b, or c.")
            print("Y coordinate should be a numeral: 1, 2, or 3.")
    return output


def handle_input(board, human: bool = True) -> int:
    if human:
        return get_user_input()
    else:
        return get_random_space(board)


def render(board):
    b = [v or ' ' for v in board]
    line = "-------\n"
    output = " |a|b|c\n"
    for x in range(3):
        output += line
        output += f"{x+1}|{b[0 + x * 3]}|{b[1 + x * 3]}|{b[2 + x * 3]}\n"
    print(output)


def update_state(board, symbol, move):
    if board[move] is not None:
        print("Move was invalid. Placing randomly.")
        board[get_random_space(board)] = symbol
    else:
        board[move] = symbol

    return game_won(board)


def run_game():
    board = [None] * 9
    players: Tuple[Player] = (Player(CROSS, True), Player(NAUGHT, False))
    # Human player is crosses, computer is naughts.
    render(board)
    for turn in range(9):
        turn_player = players[turn % 2]
        move = handle_input(board, turn_player.is_human)
        win = update_state(board, turn_player.symbol, move)
        render(board)
        if win:
            print(f"{turn_player.symbol}s wins!")
            break


run_game()
