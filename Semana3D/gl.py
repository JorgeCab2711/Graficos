from email.policy import default
import struct
from collections import namedtuple
from obj import Obj
import numpy as np
import random

V2 = namedtuple('point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])


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

    def glLine(self, v0, v1, clr=None):
        # Bresenham's algorithm
        # y = m* x + b
        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        # Si el punto cero es igual al putno uno entonces
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, clr)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        # si la linea tiene pendiente mayor a 1 o menor a menos 1
        # se intercambian las x por las y y se dibuja la linea de manera vertical
        steep = dy > dx

        # si el punto inicial x es mayor que el punto final x
        # se intercambian los puntos para siempre dibujar de izquierda a derecha
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                # dibujar de manera vertical
                self.glPoint(y, x, clr)
            else:
                # dibujarlo horizontal
                self.glPoint(x, y, clr)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1
                limit += 1

    # Funcion to check if the point is within the polygon
    def glPointInside(self, x, y, poligono):
        isInside = False
        n = len(poligono)
        x0, y0 = poligono[0]
        for j in range(n+1):
            x2, y2 = poligono[j % n]
            if y > min(y0, y2):
                if y <= max(y0, y2):
                    if x <= max(x0, x2):
                        if y0 is not y2:
                            inX = (y-y0)*(x2-x0)/(y2-y0)+x0
                        if x0 == x2 or x <= inX:
                            isInside = not isInside
            x0, y0 = x2, y2
        return isInside

    # Function to fill any polygon
    def glScanFillpoly(self, poligono, clr=None):
        for x in range(self.width):
            for y in range(self.height):
                if self.glPointInside(x, y, poligono):
                    self.glPoint(x, y, clr)

    def glCreateObjectMatrix(self, translate=V3(0, 0, 0), rotate=V3(0, 0, 0), scale=V3(1, 1, 1)):
        translate = np.matrix(
            [[1, 0, 0, translate.x],
             [0, 1, 0, translate.y],
             [0, 0, 1, translate.z],
             [0, 0, 0, 1]])

        rotation = np.identity(4)

        scaleMatrix = np.matrix(
            [[scale.x, 0, 0, 0],
             [0, scale.y, 0, 0],
             [0, 0, scale.z, 0],
             [0, 0, 0, 1]])

        return translate * rotation * scaleMatrix

    def glTransformMatrix(self, vertex, matrix):
        v = V4(vertex.x, vertex.y, vertex.z)

        vt = matrix * v

        vf = V3(vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3])

    def glLoadModel(self, filename, translate, scale):
        model = Obj(filename)

        for face in model.faces:

            vertCount = len(face)

            for vert in range(vertCount):

                v0 = model.vertices[face[vert][0] - 1]
                v1 = model.vertices[face[(vert + 1) % vertCount][0] - 1]

                x0 = round((v0[0] * scale[0]) + translate[0])
                y0 = round((v0[1] * scale[1]) + translate[1])
                x1 = round((v1[0] * scale[0]) + translate[0])
                y1 = round((v1[1] * scale[1]) + translate[1])

                self.glLine(V2(x0, y0), V2(x1, y1))
                if self.glPointInside(x0, y0, vert):
                    self.glScanFillpoly(vert)
