'''
    Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
    mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
    O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
    dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor = float(input("Valor da Hora: "))
hora = int(input("Quantidade de Horas: "))

salario_bruto = valor * hora



def descontos():
    inss = 0.10
    fgts = 0.11
    
    valor_inss = salario_bruto * inss
    valor_fgts = salario_bruto * fgts
    
    valor_ir = salario_bruto * ir

    desconto = valor_inss + valor_ir
    
    salario_liquido = salario_bruto - desconto
    
    print(f"\nSalário Bruto: ({valor} * {hora}) R$ {salario_bruto:.2f} \n(-) IR ({porcentagem}%): R$ {valor_ir:.2f}\n(-) INSS (10%): R$ {valor_inss:.2f}\nFGTS (11%): R$ {valor_fgts:.2f}\nTotal de descontos: R$ {desconto:.2f}\nSalário liquido: R$ {salario_liquido:.2f}")


if salario_bruto <= 900:
    ir = 0
    porcentagem = 0
    descontos()
elif salario_bruto <= 1500:
    ir = 0.05
    porcentagem = 5
    descontos()
elif salario_bruto <= 2500:
    ir = 0.10
    porcentagem = 10
    descontos()
else:
    ir = 0.20
    porcentagem = 20
    descontos()
    

    

