import Naive as nv
from Game import get_posible_moves, draw_board, play_move, play_turn, check_win


board: list[list[int]] = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

PLAYER = 1
COMPUTER = -1



def main():
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
        if check_win(board):
            break

        play_turn(PLAYER, board)
        draw_board(board, markers)
        n_row, n_col = nv.pick_next_move(board)
        print("Computer Turn")
        play_move(n_row, n_col, board, COMPUTER)
        draw_board(board, markers)
        

if __name__ == "__main__":
    main()

