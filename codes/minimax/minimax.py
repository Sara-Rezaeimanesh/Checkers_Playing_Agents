from copy import deepcopy
from checkers.board import Board
import pygame

RED = (255,0,0)
WHITE = (255,255,255)
INF = float('inf')
NEG_INF = float('-inf')

def minimax(position, depth, maxPlayer):
    if depth <= 0:
        return position.evaluate(), position
    
    pieceColor, v = RED, INF
    if maxPlayer:
        pieceColor, v = WHITE, NEG_INF
        
    moves ={}
    ps = position.getAllPieces(pieceColor)
    best = deepcopy(position)
    for p in ps:
        moves = position.getValidMoves(p)
        for move in moves:
            
            bcopy = deepcopy(position)
            pcopy = bcopy.getPiece(p.row, p.col)
            bcopy = simulateMove(pcopy, move, bcopy, moves[move])
            nv, nb = minimax(bcopy , depth-1, not maxPlayer)
            if (maxPlayer and v < nv) or (not maxPlayer and v > nv):
                best, v = deepcopy(bcopy), nv
    return v, best
        

def simulateMove(piece, move, board, skips):
    board.remove(skips)
    board.move(piece, move[0], move[1])
    return board