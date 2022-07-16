
from pip import main
from gl import Render, color, V2
import time

width = 1920
height = 1080


rend = Render()
rend.glCreateWindow(width, height)
# rend.glViewPort(int(width/4), int(height/4), int(width/2), int(height/2))
# rend.glClearColor(0.5, 0.5, 0.5)
# rend.glClear()
# rend.glClearViewport(color(0, 0, 0))


def extra():
    # Ciclo que mientras la variable working sea true renderizara puntos dentro del viewport dependiendo el contador
    Counter = 0
    while True:
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

def requisito():
    # Punto esquina superior derecha
    rend.glViewPortPoint(0.9999, 0.9999, color(1, 0, 0))
    # Punto centro
    rend.glViewPortPoint(0, 0, color(1, 0, 0))
    # punto esquina inferior izquierda
    rend.glViewPortPoint(-0.9999, -0.9999, color(1, 0, 0))

    rend.glFinish('output.bmp')
    print("Archivo BMP generado")

def mainMenu():
    print(
        "Ingrese cualquiera de las siguientes opciones: \n[1] Requisitos basicos\n[2] Extra"
    )
    opcion = int(input(">> "))

    if opcion == 1:
        requisito()
    elif opcion == 2:
        print("Sequencia infinita iniciada, examinar archivo BMP")
        extra()
    else:
        print('Error: Caracter desconocido dentro de las opciones.')


#mainMenu()

# m =  1
# b = int(height/2)

# for x in range(width):
#     y = m * x + b
#     y = int(y)
#     rend.glPoint(x, y)

v0 = V2(width/2 , height/2)

dy = height / 100
dX = width / 100

x = 0
y = height

for i in range(100):
    rend.glLine(V2(x,0), V2(0,y))
    rend.glLine(V2(width,height), V2(width,y))
    rend.glLine(V2(x,height), V2(width,y))

    x += dX
    y -= dy




rend.glFinish("output.bmp")

