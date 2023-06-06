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



base1 = rockNsquare.join(knightNsquareN).join(bishopNsquare).join(queenNSquare).join(kingNSquare).join(bishopNsquareN).join(knightNsquare).join(rockNsquareN)
peones12 = (pawnNsquareN.join(pawnNsquare)).horizontalRepeat(4)
jug1=base1.up(peones12)

conjunto = square.up(square.negative())
conjunto2 = conjunto.verticalRepeat(2)
conjunto3 = conjunto2.join(conjunto2.negative())
conjunto4 = conjunto3.horizontalRepeat(4)

peones2 = (pawnSquare.join(pawnSquareN)).horizontalRepeat(4)
base21 = rockSquareN.join(knightSquare).join(bishopSquareN).join(queenSquare).join(kingSquare).join(bishopSquare).join(knightSquareN).join(rockSquare)
jug2=peones2.up(base21)
draw(jug1.up(conjunto4).up(jug2))