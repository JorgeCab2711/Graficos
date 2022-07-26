import time

from sqlalchemy import true
from gl import Render, color, V2


width = 500
height = 500

rend = Render()
rend.glCreateWindow(width, height)


def drawPolygon(polygon, clr=None):
    for i in range(100):
        for idx, (x, y) in enumerate(polygon):
            polygon[idx] = V2(x, y)

        for i in range(len(polygon)):
            rend.glLine(polygon[i], polygon[(i - 1) % len(polygon)], clr)


poligon = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330),
           (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

drawPolygon(poligon, color(1, 0, 0))
rend.glPoint(100, 0, color(1, 0, 0))


rend.scanFillPolly()


# rend.glFinish("output.bmp")
