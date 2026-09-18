import math


class Operaciones:

    @staticmethod
    def calcular_longitud_circunferencia(radio):
        return 2 * math.pi * radio

    @staticmethod
    def calcular_area_circulo(radio):
        return math.pi * radio ** 2


radio = float(input("Ingrese el radio: "))

longitud = Operaciones.calcular_longitud_circunferencia(radio)
area = Operaciones.calcular_area_circulo(radio)

print("El radio es:", radio)
print("La longitud de la circunferencia es:", longitud)
print("El area del circulo es:", area)
