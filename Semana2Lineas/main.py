
from tkinter import W
from pip import main
from gl import Render, color, V2
import time


width = 1000
height = 500


rend = Render()
rend.glCreateWindow(width, height)




#mainMenu()

# m =  1
# b = int(height/2)

# for x in range(width):
#     y = m * x + b
#     y = int(y)
#     rend.glPoint(x, y)

# v0 = V2(width/2 , height/2)

# dy = height / 100
# dX = width / 100

# x = 0
# y = height

# for i in range(100):
#     rend.glLine(V2(x,0), V2(0,y))
#     rend.glLine(V2(width,height), V2(width,y))
#     rend.glLine(V2(x,height), V2(width,y))

#     x += dX
#     y -= dy

def drawSquare(width, height):
    # Square (horizontal, vertical)
    v0 = V2(width*0.2 , height*0.1)
    v1 = V2(width*0.2 ,height*0.2)
    v2 = V2(width*0.3 ,height*0.2)
    v3 = V2(width*0.3 ,height*0.1)
    rend.glLine(v0,v1)
    rend.glLine(v1,v2)
    rend.glLine(v2,v3)
    rend.glLine(v3,v0)

def drawParall(width, height):
    v0 = V2(width/2, height/2)
    v1 = V2(width*0.6, height*0.6)
    v2 = V2(width*0.4, height*0.6)
    v3 = V2(width*0.3, height/2)
    rend.glLine(v0,v1)  
    rend.glLine(v1,v2)
    rend.glLine(v2,v3)
    rend.glLine(v3,v0)

def drawPenta(width, height):
    v0 = V2(width/8, height/2)
    v1 = V2(width/4, height/2)
    v2 = V2(width*0.29, height*0.7)
    v3 = V2(width*0.199, height*0.88)
    v4 = V2(width*0.1, height*0.7)
    rend.glLine(v0,v1)  
    rend.glLine(v1,v2)
    rend.glLine(v2,v3)
    rend.glLine(v3,v4)
    rend.glLine(v4,v0)

def drawTriangle(width, height):
    v0 = V2(width*0.9, height*0.5)
    v1 = V2(width*0.7, height*0.5)
    v2 = V2(width*0.9, height*0.7)
    rend.glLine(v0,v1)  
    rend.glLine(v1,v2)
    rend.glLine(v2,v0)

def drawStar(width, height):
    v0 = V2(width*0.9, height*0.5)
    v1 = V2(width*0.85, height*0.7)
    v2 = V2(width*0.8, height*0.5)
    v3 = V2(width*0.9, height*0.65)
    v4 = V2(width*0.8, height*0.65)
    rend.glLine(v0,v1)  
    rend.glLine(v1,v2)
    rend.glLine(v2,v3)
    rend.glLine(v3,v4)
    rend.glLine(v4,v0)



# enProceso = True
# while enProceso:
#     drawPenta(width, height)
#     rend.glFinish("output.bmp")
#     time.sleep(1)
#     drawTriangle(width, height)
#     rend.glFinish("output.bmp")
#     time.sleep(1)
#     drawSquare(width, height)
#     rend.glFinish("output.bmp")
#     time.sleep(1)
#     drawParall(width, height)
#     rend.glFinish("output.bmp")
#     time.sleep(1)
#     drawStar(width, height)
#     rend.glFinish("output.bmp")
#     time.sleep(1)
#     rend.glClearColor(0.0, 0.0, 0.0) 
#     enProceso = False



