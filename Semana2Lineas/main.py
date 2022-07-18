from gl import Render, color, V2


width = 1920
height = 1080


rend = Render()
rend.glCreateWindow(width, height)


# Square
def drawSquare(width, height):
    v0 = V2(width/2, height/2)
    v1 = V2(width*0.61, height/2)
    v2 = V2(width*0.61, height*0.7)
    v3 = V2(width*0.5, height*0.7)

    rend.glLine(v0, v1, color(1, 0, 0))
    rend.glLine(v1, v2, color(1, 0, 0))
    rend.glLine(v2, v3, color(1, 0, 0))
    rend.glLine(v3, v0, color(1, 0, 0))


def drawTriangle(width, height):
    v0 = V2(width*0.15, height/4)
    v1 = V2(width/4, height/4)
    v2 = V2(width*0.15, height*0.35)

    rend.glLine(v0, v1, color(1, 0, 0))
    rend.glLine(v1, v2, color(1, 0, 0))
    rend.glLine(v2, v0, color(1, 0, 0))


def drawParallel(width, height):
    v0 = V2(width*0.75, height*0.9)
    v1 = V2(width*0.8, height*0.8)
    v2 = V2(width*0.65, height*0.8)
    v3 = V2(width*0.6, height*0.9)

    rend.glLine(v0, v1, color(0, 1, 0))
    rend.glLine(v1, v2, color(0, 1, 0))
    rend.glLine(v2, v3, color(0, 1, 0))
    rend.glLine(v3, v0, color(0, 1, 0))


def drawRombus(width, height):
    v0 = V2(width*0.1, height*0.9)
    v1 = V2(width*0.15, height*0.8)
    v2 = V2(width*0.1, height*0.7)
    v3 = V2(width*0.05, height*0.8)

    rend.glLine(v0, v1, color(0, 0, 1))
    rend.glLine(v1, v2, color(0, 0, 1))
    rend.glLine(v2, v3, color(0, 0, 1))
    rend.glLine(v3, v0, color(0, 0, 1))


def drawStar(width, height):
    v0 = V2(width*0.9, height*0.1)
    v1 = V2(width*0.85, height*0.3)
    v2 = V2(width*0.8, height*0.1)
    v3 = V2(width*0.9, height*0.25)
    v4 = V2(width*0.8, height*0.25)

    rend.glLine(v0, v1, color(1, 1, 1))
    rend.glLine(v1, v2, color(1, 1, 1))
    rend.glLine(v2, v3, color(1, 1, 1))
    rend.glLine(v3, v4, color(1, 1, 1))
    rend.glLine(v4, v0, color(1, 1, 1))


drawSquare(width, height)
drawTriangle(width, height)
drawParallel(width, height)
drawRombus(width, height)
drawStar(width, height)

rend.glFinish("output.bmp")
