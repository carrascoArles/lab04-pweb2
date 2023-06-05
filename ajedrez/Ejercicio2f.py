from interpreter import draw
from chessPictures import *

conjunto = square.up(square.negative())
conjunto2 = conjunto.verticalRepeat(2)
conjunto3 = conjunto2.join(conjunto2.negative())
conjunto4 = conjunto3.horizontalRepeat(4)
draw(conjunto4)


