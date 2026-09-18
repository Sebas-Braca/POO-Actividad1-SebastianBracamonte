import math


class Operaciones:

    @staticmethod
    def calcular_cuadrado(numero):
        return math.pow(numero, 2)

    @staticmethod
    def calcular_cubo(numero):
        return math.pow(numero, 3)


print("Calculo cuadrado y cubo de un numero")
numero = float(input("Ingrese el numero: "))

cuadrado = Operaciones.calcular_cuadrado(numero)
cubo = Operaciones.calcular_cubo(numero)

print("El numero es:", numero)
print("El cuadrado es:", cuadrado)
print("El cubo es:", cubo)
