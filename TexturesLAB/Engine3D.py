from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad

width = 1920
height = 1080

rend = Renderer(width, height)

rend.active_shader = flat
rend.active_texture = Texture("TexturesLAB/models/model.bmp")

rend.glLoadModel("TexturesLAB/models/Grass_Block.obj",
                 translate=V3(width/2, height/2, 0),
                 rotate=V3(-30, -180, -50),
                 scale=V3(200, 200, 200))

rend.glFinish("output.bmp")
