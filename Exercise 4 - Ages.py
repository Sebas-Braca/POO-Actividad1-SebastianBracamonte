import math


class Edades:

    @staticmethod
    def calcular_edad_alberto(edad_juan):
        return 2 * edad_juan / 3

    @staticmethod
    def calcular_edad_ana(edad_juan):
        return 4 * edad_juan / 3

    @staticmethod
    def calcular_edad_mama(edad_juan, edad_alberto, edad_ana):
        return edad_juan + edad_alberto + edad_ana


edad_juan = float(input("Ingrese la edad de Juan: "))

edad_alberto = Edades.calcular_edad_alberto(edad_juan)
edad_ana = Edades.calcular_edad_ana(edad_juan)
edad_mama = Edades.calcular_edad_mama(edad_juan, edad_alberto, edad_ana)

print("La edad de Juan es:", edad_juan)
print("La edad de Alberto es:", edad_alberto)
print("La edad de Ana es:", edad_ana)
print("La edad de la mama es:", edad_mama)
