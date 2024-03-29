from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
        vertical.append(value[::-1])
    return Picture(vertical)


  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for row in self.img:
        horizontal.insert(0, row)
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo = [
        ''.join(self._invColor(char) for char in value)#sirve para concatenar los caracteres invertidos en cada fila  
        for value in self.img
    ]
    return Picture(negativo)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = []
    for i in range(len(self.img)):
        join.append(self.img[i] + "" + p.img[i])
    return Picture(join)

  def up(self, p):
    image = self.img + p.img
    return Picture(image)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    image = []
    for i in range(len(self.img)):
        line = ""
        for j in range(len(self.img[i])):
            if p.img[i][j] == " ":
                line += self.img[i][j]
                
            else:line += p.img[i][j]

        image.append(line)
    return Picture(image)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repetido = []
    for i in range(len(self.img)):
        repetido.append(self.img[i] * n)
    return Picture(repetido)

  def verticalRepeat(self, n):
    repetido=self.img * n
    return Picture(repetido)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

