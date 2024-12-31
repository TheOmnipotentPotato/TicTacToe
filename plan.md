

eval function:
    +10 if x wins
    -10 if o wins
    0 if not win/draw

game board:

    -1 -> x
    1 -> o
    o -> blank

win states:
    
    rows:
        00,01,02
        10,11,12
        20,21,22
    columns:
        00,10,20
        01,11,21
        02,12,22
    
    diagonals:
        00,11,22
        02,11,20
