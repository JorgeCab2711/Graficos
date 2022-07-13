from gl import Render, color
import time
width = 512
height = 512


rend = Render()
rend.glCreateWindow(width, height)
rend.glViewPort(int(width/4), int(height/4), int(width/2), int(height/2))
rend.glClearColor(0.5, 0.5, 0.5)
rend.glClear()
rend.glClearViewport(color(0, 0, 0))

# Ciclo que mientras la variable working sea true renderizara puntos dentro del viewport dependiendo el contador
working = True
Counter = 0
while working:
    # si el contador es cero, solo se dara color al punto de la esquina superior derecha
    if (Counter == 0):
        upperRight = rend.glViewPortPoint(0.9999, 0.9999, color(1, 0, 0))
        center = rend.glViewPortPoint(0, 0, color(0, 0, 0))
        lowerLeft = rend.glViewPortPoint(-0.9999, -0.9999, color(0, 0, 0))
        Counter += 1
    # si el contador es uno solo se le dara color al punto del centro
    elif (Counter == 1):
        upperRight = rend.glViewPortPoint(0.9999, 0.9999, color(0, 0, 0))
        center = rend.glViewPortPoint(0, 0, color(1, 0, 0))
        lowerLeft = rend.glViewPortPoint(-0.9999, -0.9999, color(0, 0, 0))
        Counter += 1
    # si el contador es dos solo se le dara color al punto de la esquina inferior izquierda
    elif (Counter == 2):
        upperRight = rend.glViewPortPoint(0.9999, 0.9999, color(0, 0, 0))
        center = rend.glViewPortPoint(0, 0, color(0, 0, 0))
        lowerLeft = rend.glViewPortPoint(-0.9999, -0.9999, color(1, 0, 0))
        Counter += 1
    elif (Counter == 3):
        Counter = 0
    time.sleep(0.25)
    rend.glFinish('output.bmp')
