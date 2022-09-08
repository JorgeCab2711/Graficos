from RayTracer import Raytracer, BLACK
from RayTracer import Material
from RayTracer import Sphere
from RayTracer import color
from RayTracer import V3

coal = Material(diffuse=BLACK)
snow = Material(diffuse=color(255, 250, 250))
nose = Material(diffuse=color(255, 108, 25))

render = Raytracer(500, 500)
render.models = [
    # Ojos
    Sphere(V3(-0.64, -3.1, -10), 0.1, Material(diffuse=color(250, 250, 250))),
    Sphere(V3(0.54, -3.1, -10), 0.1, Material(diffuse=color(250, 250, 250))),
    Sphere(V3(-0.6, -3, -10), 0.25, coal),
    Sphere(V3(0.6, -3, -10), 0.25, coal),
    # Nariz
    Sphere(V3(0, -2.5, -10), 0.3, nose),
    # Boca
    Sphere(V3(-1, -2, -10), 0.15, coal),
    Sphere(V3(-0.5, -1.5, -10), 0.15, coal),
    Sphere(V3(1, -2, -10), 0.15, coal),
    Sphere(V3(0.5, -1.5, -10), 0.15, coal),
    Sphere(V3(0, -1.4, -10), 0.15, coal),
    # Botones



]


render.finish()
