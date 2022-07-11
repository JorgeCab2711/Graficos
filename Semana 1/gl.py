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
    # Object Constructor
    def __init__(self):
        self.viewPortX = 0
        self.viewPortY = 0
        self.height = 0
        self.width = 0
        self.clearColor = color(1, 1, 1)
        self.glClear()

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    # Inside object initializer function
    def glInit(self, width, height, r, g, b):
        self.width = width
        self.height = height
        self.clearColor = color(r, g, b)
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

    # Funcion para indicar el color con la que se llenara la matrix de pixeles
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, b, g)
        self.glClear()

    # Funcion para cambiar el color del fondo
    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)

    # Funcion para dibujar un punto en la matriz dew pixeles
    def glPoint(self, x, y, clr=None):
        if (0 <= x < self.width) and (0 < + y < self.height):
            self.pixels[x][y] = clr or self.currColor

    # Function to draw the viewPort square
    def viewPortSquare(self):
        for x in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for y in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.pixels[x][y] = self.currColor

    # Function to draw the viewPort

    def glViewPort(self, x, y, width, height):
        self.viewPortX = x
        self.viewPortY = y
        self.viewPortWidth = width
        self.viewPortHeight = height
        self.viewPortSquare()
