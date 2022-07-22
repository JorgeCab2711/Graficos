import time

from gl import Render, color, V2


width = 500
height = 500


rend = Render()

rend.glLoadModel('model.obj')

rend.glFinish('output.bmp')
