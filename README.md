# Basic chess AI using the negamax implementation of the minimax algorithm with alpha-beta pruning and sorting the moves in order to improve search time. Also includes a quiescence search to avoid the horizon effect.

- To run the program you need to modify the display.py file from the display package when installing it. Add this line to the beginning of the start function:

- def start(fen=''):
-   global gameboard
