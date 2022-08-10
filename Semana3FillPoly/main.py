import time


from gl import Render, color, V2


width = 1920
height = 1080
rend = Render()
rend.glCreateWindow(width, height)

star = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330),
        (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

square = [(321, 335), (288, 286), (339, 251), (374, 302)]

triangle = [(377, 249), (411, 197), (436, 249)]

pol4 = [(413, 177), (448, 159), (502, 88),
        (553, 53), (535, 36), (676, 37), (660, 52),
        (750, 145), (761, 179), (672, 192), (659, 214),
        (615, 214), (632, 230), (580, 230),
        (597, 215), (552, 214), (517, 144), (466, 180)]

pol5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

rend.drawPolygon(star, 'black')
rend.scanFillpoly(star, 'red')
rend.drawPolygon(square, 'blue')
rend.scanFillpoly(square, 'blue')
rend.drawPolygon(triangle, 'green')
rend.scanFillpoly(triangle, 'green')
rend.drawPolygon(pol4, 'black')
rend.scanFillpoly(pol4, 'black')
rend.drawPolygon(pol5, 'red')
rend.scanFillpoly(pol5, 'red')


rend.glFinish("output.bmp")
