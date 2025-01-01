from Game import check_win, get_posible_moves, play_move, score_board
from random import shuffle

class InvalidBoardState(Exception):
    pass

def pick_next_move(board: list[list[int]])->tuple[int,int]:
    if check_win(board):
       raise InvalidBoardState("Game Win has occurred") 
    moves: list[tuple[int, tuple[int, int]]] = [] 
    for row, col in get_posible_moves(board):
        score: int = hypothetical_score(board, row, col)
        moves.append((score, (row, col)))
    print(f"all moves: \n {moves}")
    tie_moves: list[tuple[int, tuple[int, int]]] = [move for move in moves if move[0] == 0]
    win_moves: list[tuple[int, tuple[int, int]]] = [move for move in moves if move[0] == -10] 
    print(f"available moves tie moves: \n {tie_moves} \n available win moves: \n {win_moves}")
    shuffle(tie_moves)
    shuffle(win_moves)
    return win_moves[0][1] if not len(win_moves) == 0 else tie_moves[0][1]

def hypothetical_score(board:list[list[int]], row: int, col: int)->int:
    _: bool
    _, board = play_move(row, col, board, -1)
    return score_board(board)

