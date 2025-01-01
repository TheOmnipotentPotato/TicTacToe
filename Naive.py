from Game import score_board, get_posible_moves, check_win, play_move

def pick_next_move(board: list[list[int]])->tuple[int,int]:
    moves: list[tuple[int, tuple[int, int]]] = [] 
    print(board)
    for row, col in get_posible_moves(board):
        score: int = hypothetical_score(board, row, col)
        moves.append((score, (row, col)))
        print(board)
    moves.sort(key= (lambda x : x[0]))
    return moves[0][1]

def hypothetical_score(board:list[list[int]], row: int, col: int)->int:
    board_copy = board[:]
    # (for oliver and matt) this is how you copy list in python
    # i can explain why this is needed if you like
    _ = play_move(row, col, board_copy, -1)
    return score_board(board_copy)

