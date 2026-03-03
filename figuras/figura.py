class Figura:
    def __init__(self, nombre="", color=""):
        self.nombre = nombre
        self.color = color

    def leer(self):
        self.nombre = input("Forma: ")
        self.color = input("Color: ")

