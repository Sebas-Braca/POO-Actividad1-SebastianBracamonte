class Operaciones:

    @staticmethod
    def operacion1(suma, x):
        return suma + x

    @staticmethod
    def operacion2(x, y):
        return x + y ** 2

    @staticmethod
    def operacion3(suma, x, y):
        return suma + (x / y)


suma = 0
x = 20
y = 40

suma = Operaciones.operacion1(suma, x)
x = Operaciones.operacion2(x, y)
suma = Operaciones.operacion3(suma, x, y)

print("El valor de la suma es:", suma)
