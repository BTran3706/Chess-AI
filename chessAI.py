import chess
from chessboard import display
import operator

#Score pieces based on their position. Piece tables can be found online
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
    -10, 0, 0, 0, 0, 0, 0, -10,
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

def evaluateBoard():
    
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    elif board.is_stalemate():
        return 0
    elif board.is_insufficient_material():
        return 0

    #Number of each pieces
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

    #Pawns are worth 100, knights worth 320, bishops worth 330, rooks worth 500 and queens worth 900
    material = 100 * (whitePawn - blackPawn) + 320 * (whiteKnight - blackKnight) + 330 * (whiteBishop - blackBishop) + 500 * (whiteRook - blackRook) + 900 * (whiteQueen - blackQueen)

    pawnScore = sum([pawnTable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnScore -= sum([pawnTable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])

    knightScore = sum([knightTable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightScore -= sum([knightTable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])

    bishopScore = sum([bishopTable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopScore -= sum([bishopTable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])

    rookScore = sum([rookTable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rookScore -= sum([rookTable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])

    queenScore = sum([queenTable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queenScore -= sum([queenTable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])

    kingScore = sum([kingTable[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingScore -= sum([kingTable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])

    evaluation = material + pawnScore + knightScore + bishopScore + rookScore + queenScore + kingScore

    if board.turn:
        return evaluation
    else:
        return -evaluation

# Search best move using minimax and alphabeta algorithm with negamax implementation
def negamax(alpha, beta, depth):

    if depth == 0:
        return quiescence(alpha, beta)

    bestScore = -9999
    moveValuePair = sortMoves(False)

    for move in moveValuePair:
        board.push(move)
        score = -negamax(-beta, -alpha, depth - 1)
        board.pop()
        if score >= beta:
            return score
        if score > bestScore:
            bestScore = score
        if score > alpha:
            alpha = score

    return bestScore

#Used to get rid of horizon effect
def quiescence(alpha, beta):

    score = evaluateBoard()

    if score >= beta:
        return beta

    if score > alpha:
        alpha = score

    moveValuePair = sortMoves(True)

    for move in moveValuePair:
        board.push(move)    
        score = -quiescence(-beta, -alpha)
        board.pop()
        if score >= beta:
            return beta
        elif score > alpha:
            alpha = score

    return alpha

#Sort moves in ascending order based on their board value
def sortMoves(capturesOnly):
    
    moveValuePair = {}

    if not capturesOnly:
        for move in board.legal_moves:
            board.push(move)
            moveValuePair[move] = evaluateBoard()
            board.pop()
    else:
        for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                moveValuePair[move] = evaluateBoard()
                board.pop()

    sortMoveValuePair = dict(sorted(moveValuePair.items(), key = operator.itemgetter(1)))

    return sortMoveValuePair

def selectMove(depth):
    
    bestValue = -99999
    alpha = -100000
    beta = 100000

    for move in board.legal_moves:
        board.push(move)
        boardValue = -negamax(-beta, -alpha, depth - 1)
        board.pop()
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue

    return bestMove

#Main Function
board = chess.Board()
display.start(board.fen())

while not display.checkForQuit():
    if not board.is_game_over():
        #Uncomment if you want to play against AI where you type your move
        #playerMove = input()
        #board.push_san(playerMove)
        #display.update(board.fen())
        move = selectMove(3)
        board.push(move)
        display.update(board.fen())
        print(move)

display.terminate()
