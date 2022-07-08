from gl import Renderer

rend = Renderer(512, 512)

rend.glClearColor(1,0,0)


rend.glFinish('output.bmp')