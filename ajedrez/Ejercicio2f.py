from interpreter import draw
from chessPictures import *

conjunto = square.up(square.negative())
conjunto2 = conjunto.verticalRepeat(2)

draw(conjunto2)


