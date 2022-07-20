from re import X
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
        
        for idx, (x, y) in enumerate(polygon):
            polygon[idx] = (x-1, y-1)



    
    




poligon = [(165, 380),(185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

def restarATupla(tupla):
    greater = int(0)
    if tupla[0] > tupla[1]:
        greater = tupla[0]
    else:
        greater = tupla[1]

    print(greater)

tupla = (1,2)
restarATupla(tupla)


#drawPolygon(poligon, color(1, 0, 0))



rend.glFinish("output.bmp")
