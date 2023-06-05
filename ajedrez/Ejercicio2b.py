from interpreter import draw
from chessPictures import *
knightN = knight.negative()
conjunto1 = knight.join(knightN)
knightN2 = knightN.verticalMirror()
conjunto2 = knightN2.join(knight.verticalMirror())
conjunto = conjunto1.up(conjunto2)

draw(conjunto)
