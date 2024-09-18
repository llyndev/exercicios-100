# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Digite seu salario: "))
horas_trabalhada = int(input("Digite a quantidade de horas trabalhadas: "))

salario = salario_hora * horas_trabalhada

print(f"Salario: R${salario:.2f}")