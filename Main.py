import Naive as nv
from Game import get_posible_moves, draw_board, play_move, play_turn, check_win


board: list[list[int]] = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

PLAYER = 1
COMPUTER = -1



def main(board: list[list[int]]):
    print("Pick your marker (x | o): \n")
    marker: str = str(input())
    stupid: list[str] = ["x", "o"]
    stupid.remove(marker)
    markers: dict[int,str] = {
        PLAYER: marker,
        COMPUTER :  stupid[0] ,
        0 : " ",

    }
    draw_board(board, markers)
    while True:
        if len(get_posible_moves(board)) == 0:
            break
        win: int = check_win(board)
        if win:
            print(f"{"Player" if win == 1 else "Computer"} wins")
            break

        board = play_turn(PLAYER, board)
        draw_board(board, markers)
        try:
            n_row, n_col = nv.pick_next_move(board)
        except nv.InvalidBoardState:
            continue
        print("Computer Turn")
        _: bool
        _, board = play_move(n_row, n_col, board, COMPUTER)
        draw_board(board, markers)
        

if __name__ == "__main__":
    main(board)

