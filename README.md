# Personal project where I created a basic chess AI using the negamax implementation of the minimax algorithm with alpha-beta pruning and sorting the moves in order to improve search time. Also includes a quiescence search to avoid the horizon effect.

To run the program, you need to install the chess and chessboard libraries.
- python -m pip install chess
- python -m pip install chessboard

You also have to modify the display.py file from the chessboard and display package as well or there will be an error. Add this line to the beginning of the start function:

def start(fen=''):

      global gameboard
      
Here is a YouTube video of myself explaining how the minimax and negamax algorithms work:  
      https://youtu.be/GPUywlsxYKc
