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

kingEndTable = [
    -50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30, 0, 0, 0, 0, -30,-30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50]

def evaluateScore():
    
    if board.is_checkmate():
        if board.turn: #If White turn, return -9999 meaning Black won. Else return 9999 meaning White won
            return -9999
        else:
            return 9999

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

    pawnScore = sum([pawnTable[i] for i in board.pieces(chess.PAWN, chess.WHITE)]) - sum([pawnTable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightScore = sum([knightTable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)]) - sum([knightTable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopScore = sum([bishopTable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)]) - sum([bishopTable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rookScore = sum([rookTable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) - sum([rookTable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])
    queenScore = sum([queenTable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) - sum([queenTable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])
    
    if 100 * whitePawn + 300 * whiteKnight + 300 * whiteBishop + 500 * whiteRook + 900 * whiteQueen < 1400 and 100 * blackPawn + 300 * blackKnight + 300 * blackBishop + 500 * blackRook + 900 * blackQueen < 1400:
        #If materialScore on both sides are less than 1400 (queen + rook), use kingEndTable
        kingScore = sum([kingEndTable[i] for i in board.pieces(chess.KING, chess.WHITE)]) - sum([kingEndTable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])
    else:
        kingScore = sum([kingTable[i] for i in board.pieces(chess.KING, chess.WHITE)]) - sum([kingTable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])

    #Pawns are worth 100, knights 300, bishops 375, rooks 500 and queen 900
    materialScore = 100 * (whitePawn - blackPawn) + 300 * (whiteKnight - blackKnight) + 375 * (whiteBishop - blackBishop) + 500 * (whiteRook - blackRook) + 900 * (whiteQueen - blackQueen)
    totalScore = materialScore + pawnScore + knightScore + bishopScore + rookScore + queenScore + kingScore

    if board.turn: #Return positive score if White turn. Negative score if Black turn
        return totalScore
    else:
        return -totalScore

#Search best move using minimax and alphabeta algorithm with negamax implementation
def negamax(alpha, beta, depth):

    if depth == 0:
        return quiescence(alpha, beta)

    bestScore = -9999 #Initialize bestScore as worst possible White score
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

    bestScore = -99999 #Initialize bestScore as worst possible White score
    alpha = -100000 #Alpha is bestScore for the maximizing player (White). Initialize as worst possible White score
    beta = 100000 #Beta is bestScore for the minimizing player (Black). Initialize as worst possible Black score

    for move in board.legal_moves:
        if board.is_castling(move): #Don't need to check castling rights if the move is a castle
            board.push(move)
            if board.turn and len(board.pieces(chess.BISHOP, chess.BLACK)) == 1: #Subtract 50 (Value of half pawn) if AI has only 1 bishop
                moveScore = -negamax(-beta, -alpha, depth - 1) - 50
            elif not board.turn and len(board.pieces(chess.BISHOP, chess.WHITE)) == 1:
                moveScore = -negamax(-beta, -alpha, depth - 1) - 50
            else:
                moveScore = -negamax(-beta, -alpha, depth - 1)
        else:
            if board.turn:
                castleRightsBefore = board.has_castling_rights(chess.WHITE) #Compare castle rights before and after. If before is true and after is false then the move prevents castling
                board.push(move)
                castleRightsAfter = board.has_castling_rights(chess.WHITE)
                numBishops = len(board.pieces(chess.BISHOP, chess.WHITE))
            else:
                castleRightsBefore = board.has_castling_rights(chess.BLACK)
                board.push(move)
                castleRightsAfter = board.has_castling_rights(chess.BLACK)
                numBishops = len(board.pieces(chess.BISHOP, chess.BLACK))
            if numBishops == 1 and castleRightsBefore and not castleRightsAfter: #Subtract 100 (Value of 1 pawn) if AI has only 1 bishop and if the move prevents castling
                moveScore = -negamax(-beta, -alpha, depth - 1) - 100
            elif castleRightsBefore and not castleRightsAfter: #Subtract 50 (Value of half pawn) if the move prevents castling
                moveScore = -negamax(-beta, -alpha, depth - 1) - 50
            else:
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
        if board.is_checkmate():
            if board.turn:
                print("BLACK WON!")
            else:
                print("WHITE WON!")
        else:
            print("STALEMATE/DRAW!")
        printEndMessage = True

display.terminate()
