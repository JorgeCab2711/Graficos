from gl import Render

width = 500
height = 500


rend = Render()
rend.glCreateWindow(width, height)
# rend.glViewPort(7, 7, 500, 500)

for i in range(width):
    rend.glPoint(i, i)


rend.glFinish('output.bmp')
