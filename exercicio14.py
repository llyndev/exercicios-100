'''
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    - salário bruto. 
    - quanto pagou ao INSS. 
    - quanto pagou ao sindicato. 
    - o salário líquido. 
    - calcule os descontos e o salário líquido, conforme a tabela abaixo: 
'''

salario_hora = float(input("Informe o valor que você recebe por hora: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))

salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto - (salario_bruto * 0.89)
inss = salario_bruto - (salario_bruto * 0.92)
sindicato = salario_bruto - (salario_bruto * 0.95)
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"+ Salario Bruto: R$ {salario_bruto:.2f}")
print(f"- IR: R$ {ir:.2f}")
print(f"- INSS: R$ {inss:.2f}")
print(f"- Sindicato: R$ {sindicato:.2f}")
print(f"- Total Descontos: R$ {descontos:.2f}")
print(f"= Salario Líquido: R$ {salario_liquido:.2f}")

