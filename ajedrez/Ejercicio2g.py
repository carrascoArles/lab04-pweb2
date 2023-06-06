from interpreter import draw
from chessPictures import *
#primero crear todas las variables a usar

bishopN = bishop.negative()
knightN = knight.negative()
rockN = rock.negative()
kingN = king.negative()
queenN = queen.negative()
pawnN = pawn.negative()
squareN = square.negative()

#fichas blancas en sus cuadrados
rockSquare = square.under(rock)
knightSquare = square.under(knight)
bishopSquare = square.under(bishop)
pawnSquare = square.under(pawn)
queenSquare = square.under(queen)

rockSquareN = squareN.under(rock)
knightSquareN = squareN.under(knight)
bishopSquareN = squareN.under(bishop)
pawnSquareN = squareN.under(pawn)
kingSquare = squareN.under(king)

#fichas negras en sus cuadrados
rockNsquare = square.under(rockN)
knightNsquare = square.under(knightN)
bishopNsquare = square.under(bishopN)
pawnNsquare = square.under(pawnN)
kingNSquare = square.under(kingN)

rockNsquareN = squareN.under(rockN)
knightNsquareN = squareN.under(knightN)
bishopNsquareN = squareN.under(bishopN)
pawnNsquareN = squareN.under(pawnN)
queenNSquare = squareN.under(queenN)
