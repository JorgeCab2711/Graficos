class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.textcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                prefix, value = line.split(' ', 1)
            except:
                continue

            if prefix == 'v':
                self.vertices.append(list(map(float, value.split(' '))))
            elif prefix == 'vt':
                self.textcoords.append(list(map(float, value.split(' '))))
            elif prefix == 'vn':
                self.normals.append(list(map(float, value.split(' '))))
            elif prefix == 'f':
                self.faces.append([vert.split('/')
                                  for vert in value.split(' ')])

        for face in self.faces:
            print(face)
