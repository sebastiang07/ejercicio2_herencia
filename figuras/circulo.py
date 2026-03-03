import math

from figuras.figura import Figura


class Circulo(Figura):
    def __init__(self, color="", radio=0):
        super().__init__("Círculo", color)
        self.radio = radio

    def leer(self):
        self.nombre = "Círculo"
        self.color = input("Color: ")
        self.radio = float(input("Radio: "))

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def mostrar_datos(self):
        print(f"Forma: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Radio: {self.radio:g}")
        print(f"Área: {self.calcular_area():.2f}")
