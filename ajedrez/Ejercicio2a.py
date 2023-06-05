from interpreter import draw
from chessPictures import *
knightN = knight.negative()
conjunto1 = knight.join(knightN)
conjunto2 = knightN.join(knight)
conjunto = conjunto1.up(conjunto2)

draw(conjunto)
