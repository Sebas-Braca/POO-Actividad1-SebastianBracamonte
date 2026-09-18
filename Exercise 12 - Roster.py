class Nomina:

    @staticmethod
    def calcular_salario_bruto(horas_laboradas, valor_hora):
        return horas_laboradas * valor_hora

    @staticmethod
    def calcular_valor_retefuente(salario_bruto, porcentaje_retencion):
        return salario_bruto * porcentaje_retencion / 100

    @staticmethod
    def calcular_salario_neto(salario_bruto, retefuente):
        return salario_bruto - retefuente


horas_laboradas = 48
valor_hora = 5000
porcentaje_retencion = 12.5

salario_bruto = Nomina.calcular_salario_bruto(horas_laboradas, valor_hora)
retefuente = Nomina.calcular_valor_retefuente(salario_bruto, porcentaje_retencion)
salario_neto = Nomina.calcular_salario_neto(salario_bruto, retefuente)

print("El salario bruto es:", salario_bruto)
print("La retencion en la fuente es:", retefuente)
print("El salario neto es:", salario_neto)
