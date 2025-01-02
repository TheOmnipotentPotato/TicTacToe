# MiniMax

## procedure:

1. take in game state
2. generate decision tree of depth 4 (2 mini 2 max layers)
3. score leaves
4. backtrack and score nodes 
    4.1 based upon the children of the node pick either the 
    high or low score
    \newline
    4.2 backtrack up the tree alternating between min and max
    pick
5. once layer 1 is scored pick optimal choice

## example with two layers
Computer is playing as `o` and it is their turn

    Current Board State
    
    x - x
    o o -
    o x -

    Possible Next Moves for Computer(o)

    x o x             x - x             x - x 
    o o -             o o -             o o o 
    o x -             o x o             o x - 
    ( 0 )             ( -10 )           ( 10 )
    Potential Reactions from Player(x)

    x o x   x o x     x - x   x x x     (previous game win) 
    o o x   o o -     o o x   o o -     (no generation after)
    o x -   o x x     o x o   o x o     
    ( 0 )   ( 0 )     ( 0 )   ( -10 )
    
