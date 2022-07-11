from gl import Render

rend = Render()
rend.glCreateWindow(500, 500)
rend.glViewPort(7, 7, 500, 500)

rend.glFinish('output.bmp')
