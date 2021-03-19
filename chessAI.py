import chess
from chessboard import display

#Score pieces based on their position. Piece square tables can be found online
pawnTable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knightTable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

bishopTable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rookTable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

queenTable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

kingTable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

def evaluateScore():
    
    if board.is_checkmate():
        if board.turn: #If white turn, return -9999 meaning black won. Else return 9999 meaning white won
            return -9999
        else:
            return 9999
    elif board.is_stalemate():
        return 0
    elif board.is_insufficient_material():
        return 0

    pawnScore = sum([pawnTable[i] for i in board.pieces(chess.PAWN, chess.WHITE)]) - sum([pawnTable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightScore = sum([knightTable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)]) - sum([knightTable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopScore = sum([bishopTable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)]) - sum([bishopTable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rookScore = sum([rookTable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) - sum([rookTable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])
    queenScore = sum([queenTable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) - sum([queenTable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingScore = sum([kingTable[i] for i in board.pieces(chess.KING, chess.WHITE)]) - sum([kingTable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])
   
    #Number of each pieces based on current board state
    whitePawn = len(board.pieces(chess.PAWN, chess.WHITE))
    blackPawn = len(board.pieces(chess.PAWN, chess.BLACK))
    whiteKnight = len(board.pieces(chess.KNIGHT, chess.WHITE))
    blackKnight = len(board.pieces(chess.KNIGHT, chess.BLACK))
    whiteBishop = len(board.pieces(chess.BISHOP, chess.WHITE))
    blackBishop = len(board.pieces(chess.BISHOP, chess.BLACK))
    whiteRook = len(board.pieces(chess.ROOK, chess.WHITE))
    blackRook = len(board.pieces(chess.ROOK, chess.BLACK))
    whiteQueen = len(board.pieces(chess.QUEEN, chess.WHITE))
    blackQueen = len(board.pieces(chess.QUEEN, chess.BLACK))

    #Pawns are worth 100, knights 300, bishops 310, rooks 500 and queen 900
    piecesScore = 100 * (whitePawn - blackPawn) + 300 * (whiteKnight - blackKnight) + 310 * (whiteBishop - blackBishop) + 500 * (whiteRook - blackRook) + 900 * (whiteQueen - blackQueen)
    totalScore = piecesScore + pawnScore + knightScore + bishopScore + rookScore + queenScore + kingScore

    if board.turn: #Return positive score if white turn. Negative score if black turn
        return totalScore
    else:
        return -totalScore

#Search best move using minimax and alphabeta algorithm with negamax implementation
def negamax(alpha, beta, depth):

    if depth == 0:
        return quiescence(alpha, beta)

    bestScore = -9999 #Initialize bestScore as worst possible score in terms of White
    moveValuePair = sortMoves(False)

    for move in moveValuePair:
        board.push(move)
        moveScore = -negamax(-beta, -alpha, depth - 1)
        board.pop()
        bestScore = max(bestScore, moveScore)
        alpha = max(alpha, moveScore)
        if beta <= alpha:
            return bestScore

    return bestScore

#Used to get rid of horizon effect
def quiescence(alpha, beta):

    moveScore = evaluateScore()
    alpha = max(alpha, moveScore)
    
    if beta <= alpha:
            return moveScore

    moveValuePair = sortMoves(True)

    for move in moveValuePair:
        board.push(move)    
        moveScore = -quiescence(-beta, -alpha)
        board.pop()
        alpha = max(alpha, moveScore)
        if beta <= alpha:
            return moveScore

    return alpha

#Sort moves in ascending order based on their score
def sortMoves(capturesOnly):
    
    moveValuePair = {}

    if capturesOnly:
        for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                moveValuePair[move] = evaluateScore()
                board.pop()
    else:
        for move in board.legal_moves:
            board.push(move)
            moveValuePair[move] = evaluateScore()
            board.pop()

    sortMoveValuePair = dict(sorted(moveValuePair.items(), key = lambda item: item[1]))

    return sortMoveValuePair

def selectMove(depth):
    
    bestMove = chess.Move.null()
    bestScore = -9999 #Initialize bestScore as worst possible score in terms of White
    alpha = -9999 #Alpha is bestScore for the maximizing player (White). Initialize as worst possible score in terms of White
    beta = 9999 #Beta is bestScore for the minimizing player (Black). Initialize as worst possible score in terms of Black

    for move in board.legal_moves:
        board.push(move)
        moveScore = -negamax(-beta, -alpha, depth - 1)
        board.pop()
        if moveScore > bestScore:
            bestScore = moveScore
            bestMove = move
        alpha = max(alpha, moveScore)

    return bestMove

#Main Function
board = chess.Board()
display.start(board.fen())
printEndMessage = False

while not display.checkForQuit():
    if not board.is_game_over():
        #Uncomment if you want to play vs AI by typing move. A move is starting square of piece you want to move followed by square where you want piece to move to. Ex: e2e4 moves pawn on e2 to e4
        #playerMove = input()
        #board.push(playerMove)
        #display.update(board.fen())
        AImove = selectMove(3) #Increase number for harder AI at the cost of it taking longer
        board.push(AImove)
        display.update(board.fen())
        print(AImove)
    elif not printEndMessage:
        if board.turn:
            print("BLACK WON!")
        else:
            print("WHITE WON!")
        printEndMessage = True

display.terminate()
