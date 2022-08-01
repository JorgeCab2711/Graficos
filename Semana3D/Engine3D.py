from gl import Render, color

from obj import Obj

width = 1920
height = 1080


r = Render()
r.glCreateWindow(width, height)

r.glLoadModel('./Semana3D/Models/Shrek.obj', (width/2, height/4), (600, 600))

r.glFinish('output.bmp')
