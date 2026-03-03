from figuras.figura import Figura


class Triangulo(Figura):
    def __init__(self, color="", base=0, altura=0):
        super().__init__("Triángulo", color)
        self.base = base
        self.altura = altura

    def leer(self):
        self.nombre = "Triángulo"
        self.color = input("Color: ")
        self.base = float(input("Base: "))
        self.altura = float(input("Altura: "))

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def mostrar_datos(self):
        print(f"Forma: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Base: {self.base:g}")
        print(f"Altura: {self.altura:g}")
        print(f"Área: {self.calcular_area():g}")
