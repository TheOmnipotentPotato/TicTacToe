from Game import get_posible_moves, draw_board, play_move, play_turn, check_win, score_board, PLAYER, COMPUTER
from copy import deepcopy

class MoveNode:
    def __init__(self, *args):
        #row:int, col:int, player:int, parent_board:list[list[int]]
        if(len(args) == 4):
            self.move: tuple[int,int] = (args[0], args[1])
            self.player: int = args[2]
            self.future_moves: list[MoveNode] = []
            self.score: int|None = None
            self.board: list[list[int]] = deepcopy(args[3])
            _, self.board = play_move(self.move[0], self.move[1], self.board, self.player)
        #board:list[list[int]], player:int
        if(len(args) == 2): 
            self.move: None = None
            self.player: int = args[0]
            self.future_moves: list[MoveNode] = []
            self.score:int|None = None
            self.board:list[list[int]] = args[1]
        else:
            raise TypeError("Improper argument pass. \n Pass arguments either as row:int, col:int, player:int, parent_board:list[list[int]] for non root nodes or \n board:list[list[int]], player:int for the root node")
        return


    def generate_next_round(self):
        if check_win(self.board):
            return
        posible_moves: list[tuple[int,int]] = get_posible_moves(self.board)
        def add_child(move:tuple[int, int])->None:
            self.future_moves.append(MoveNode(move[0], move[1], -self.player, self.board))
            return
        for move in posible_moves:
            add_child(move)
        return
    
    def score_moves(self):
        def compare_by_score(move:MoveNode)->int:
            if move.score is None:
                raise ValueError("Score is Null")
            return move.score
        if len(self.future_moves) == 0:
            self.score = score_board(self.board)
            return
        
        if self.player == PLAYER:
            #maximizer branch
            self.score = max(self.future_moves, key = compare_by_score).score
        elif self.player == COMPUTER:
            #minimizer branch
            self.score = min(self.future_moves, key = compare_by_score).score









