import time

from sqlalchemy import true
from gl import Render, color, V2


width = 500
height = 500
rend = Render()
rend.glCreateWindow(width, height)

star = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330),
        (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

rend.drawPolygon(star, 'blue')
rend.scanFillpoly(star, 'red')


rend.glFinish("output.bmp")
