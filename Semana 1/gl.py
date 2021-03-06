import struct


def char(c):
    # 1 byte length
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes length
    return struct.pack('=h', w)


def dword(d):
    # 3 bytes length
    return struct.pack('=l', d)


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


class Render(object):
    # Constructor del Objecto
    def __init__(self):
        self.viewPortX = 0
        self.viewPortY = 0
        self.height = 0
        self.width = 0
        self.clearColor = color(0, 0, 0)
        self.currColor = color(1, 1, 1)
        self.glViewPort(0, 0, self.width, self.height)

        self.glClear()

    # Funcion para crear una ventana definiendo su alto y ancho
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    # Function to create a BMP file
    def glFinish(self, filename):
        with open(filename, 'wb') as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))

            # file size
            file.write(dword(14 + 40 + self.height * self.width * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # Info Header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
            file.close()

    # Funcion para llenar el color del fondo utilizando la matriz de pixeles

    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)]
                       for x in range(self.width)]

    def glClearViewport(self, clr=None):
        for i in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for j in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.glPoint(i, j, clr)

    # Funcion para indicar el color con la que se llenara la matrix de pixeles

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, b, g)
        self.glClear()

    # Funcion para cambiar el color del fondo
    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)

    # Funcion para dibujar un punto en la matriz dew pixeles en cualquier parte de la ventana
    def glPoint(self, x, y, clr=None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor

    # Funcion para crear un viewport dentro de la matrix
    def glViewPort(self, posX, posY, width, height):
        self.viewPortX = posX
        self.viewPortY = posY
        self.viewPortWidth = width
        self.viewPortHeight = height

    # Funcion para crear un punto dentro de los limites del punto con coordenadas normalizadas
    def glViewPortPoint(self, normX, normY, clr=None):
        # Verifica la posicion del punto llegando a 0.9999 por alguna razon cuando es 1 se sale del viewport
        if normX > 0.9999 or normX < -0.9999 or normY > 0.9999 or normY < -0.9999:
            print('Warning, coordinates out of viewport range.')
        else:
            x = (normX + 1) * (self.viewPortWidth/2) + self.viewPortX
            y = (normY + 1) * (self.viewPortHeight/2) + self.viewPortY

            x = int(x)
            y = int(y)

            self.glPoint(x, y, clr)
