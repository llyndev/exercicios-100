# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input("Digite um número: "))

lista = [1, 2, 3, 4, 5, 6, 7]

if num in lista:
    if num == 1:
        print('Domingo')
    if num == 2:
        print('Segunda')
    if num == 3:
        print('Terça')
    if num == 4:
        print('Quarta')
    if num == 5:
        print('Quinta')
    if num == 6:
        print('Sexta')
    if num == 7:
        print('Sábado')
else:
    print('Número inválido')