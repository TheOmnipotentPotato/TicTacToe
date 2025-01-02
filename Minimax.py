
from typing import override
from Game import draw_board, get_posible_moves, play_move, check_win, score_board, to_string, PLAYER, COMPUTER
from copy import deepcopy

class InvalidBoardState(Exception):
    pass

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
        elif(len(args) == 2): 
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
        return
    @override        
    def __str__(self)->str:
        return f"board: {self.board} \n score: {self.score}"
class DecisionTree:
    def __init__(self, board:list[list[int]], player:int, depth:int=2):
        self.root:list[MoveNode] = [MoveNode(player, board)]
        self.depth:int = depth
    
    def next_move(self)->tuple[int,int]:
        DecisionTree.build_tree(self.root, 0, 2)
        DecisionTree.score_tree(self.root)
        moves:list[MoveNode] = self.root[0].future_moves 
        tie_moves: list[MoveNode] = [move for move in moves if move.score == 0]
        win_moves: list[MoveNode] = [move for move in moves if move.score == -10] 
        
        return win_moves[0].move if not len(win_moves) == 0 else tie_moves[0].move #type: ignore

    @classmethod
    def build_tree(cls, nodes:list[MoveNode], cur_depth:int, goal_depth:int):
        if cur_depth > goal_depth:
            return
        for node in nodes:
            node.generate_next_round()
            DecisionTree.build_tree(node.future_moves, cur_depth+1, goal_depth)
        return
    
    @classmethod
    def score_tree(cls, nodes:list[MoveNode]):
        print(" ".join([str(node.board) for node in nodes]))
        for node in nodes:
            DecisionTree.score_tree(node.future_moves)
            node.score_moves()
            print(node.score)
            if(node.score != 0):
                print("<===================>\n score:" + str(node.score))
                draw_board(node.board, {
                    PLAYER: "x",
                    COMPUTER: "o",
                    0 : " "
                })
                print("<===================>")
        return


    @override
    def __str__(self)->str:
        raise NotImplementedError


def pick_next_move(board: list[list[int]])->tuple[int,int]:
    if check_win(board):
       raise InvalidBoardState("Game Win has occurred") 
    tree: DecisionTree = DecisionTree(board, COMPUTER)
    return tree.next_move()
    


if __name__ == "__main__":
    board = [
        [-1,0,0],
        [ 0,0,1],
        [-1,0,0],
    ]
    tree = DecisionTree(board, COMPUTER)
    DecisionTree.build_tree(tree.root, 0, 2)
    DecisionTree.score_tree(tree.root)



