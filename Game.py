from copy import deepcopy

PLAYER = 1
COMPUTER = -1

def check_win(board: list[list[int]])->int:
    b = lambda row,column : board[row][column]
    states = (
        (b(0,0), b(0,1), b(0,2)),
        (b(1,0), b(1,1), b(1,2)),
        (b(2,0), b(2,1), b(2,2)),
        (b(0,0), b(1,0), b(2,0)),
        (b(0,1), b(1,1), b(2,1)),
        (b(0,2), b(1,2), b(2,2)),
        (b(0,0), b(1,1), b(2,2)),
        (b(0,2), b(1,1), b(2,0)),
    )

    if (PLAYER,PLAYER, PLAYER) in states:
        return PLAYER

    elif (COMPUTER, COMPUTER, COMPUTER) in states:
        return COMPUTER

    return 0

def score_board(board: list[list[int]])->int:
    return check_win(board)*10

def get_posible_moves(board:list[list[int]])->list[tuple[int,int]]:
    valid_moves: list[tuple[int,int]] = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                valid_moves.append((x,y))

    return valid_moves

def play_move(row:int, column:int, board: list[list[int]], player: int)->tuple[bool, list[list[int]]]:
    copy: list[list[int]] = deepcopy(board)
    if not copy[row][column] == 0:
        return False, copy
    
    copy[row][column] = player
    return True, copy

def draw_board(board: list[list[int]], markers:dict[int,str])->None:
    def tran(row: int, column: int)->str|None:
        return markers.get(board[row][column])

    print("+-+-+-+")
    print(f"|{tran(0,0)}|{tran(0,1)}|{tran(0,2)}|")
    print("+-+-+-+")
    print(f"|{tran(1,0)}|{tran(1,1)}|{tran(1,2)}|")
    print("+-+-+-+")
    print(f"|{tran(2,0)}|{tran(2,1)}|{tran(2,2)}|")
    print("+-+-+-+")
    
    return

def to_string(board:list[list[int]], markers:dict[int,str])->str:
    def tran(row: int, column: int)->str|None:
        return markers.get(board[row][column])

    out:str = "+-+-+-+\n"+\
    f"|{tran(0,0)}|{tran(0,1)}|{tran(0,2)}|\n"+\
    "+-+-+-+\n"+\
    f"|{tran(1,0)}|{tran(1,1)}|{tran(1,2)}|\n"+\
    "+-+-+-+\n"+\
    f"|{tran(2,0)}|{tran(2,1)}|{tran(2,2)}|\n"+\
    "+-+-+-+"
    return out


def play_turn(player:int, board:list[list[int]])->list[list[int]]:
    cell:int = int(input("Pick a cell(1-9): ")) - 1
    if cell < 0 or cell > 8:
        print("Outside Range")
        return play_turn(player, board)
    print(f"{cell//3}, {cell%3}")
    moved: bool 
    copy: list[list[int]]
    moved, copy = play_move(cell//3, cell%3, board, player)
    if not moved:
        print("Invalid move")
        return play_turn(player, board)
    print("Move Success")
    return copy


