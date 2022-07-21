import time
from gl import Render, color, V2


width = 500
height = 500


rend = Render()
rend.glCreateWindow(width, height)


def drawPolygon(polygon, clr =  None):
    for i in range(100):
        for idx, (x, y) in enumerate(polygon):
            polygon[idx] = V2(x, y)

        for i in range(len(polygon)):
            rend.glLine(polygon[i], polygon[(i - 1) % len(polygon)], clr)
        

poligon = [(165, 380),(185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

#drawPolygon(poligon, color(1, 0, 0))

# x0 = 0
# y0 = 0
# x1 = width
# y1 = 0

# color_one = color(1, 0, 0)

# for i in range(width):
#     if y0 < height:
#         rend.glLine(V2(x0,y0), V2(x1, y1), color_one)
#         y0 += 1
#         y1 += 1
#         print("works")
#         #time.sleep(0.5)
#     else:
#         pass



    
rend.glFinish("output.bmp")
