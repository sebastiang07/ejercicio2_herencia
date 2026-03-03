from figuras.circulo import Circulo
from figuras.triangulo import Triangulo


def main():
    circulo = Circulo(color="Azul", radio=5)
    triangulo = Triangulo(color="Verde", base=10, altura=8)

    circulo.mostrar_datos()
    print()
    triangulo.mostrar_datos()


if __name__ == "__main__":
    main()

