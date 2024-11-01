'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:

    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''

t1 = int(input('Digite o 1º lado do triângulo: '))
t2 = int(input('Digite o 2º lado do triângulo: '))
t3 = int(input('Digite o 3º lado do triângulo: '))

if t1 == 0 or t2 == 0 or t3 == 0:
    print('Um dos lados do triângulo é igual a zero!')
    
if t1 == t2 and t1 == t3 and t2 == t3:
    print('Triângulo Equilátero!')
elif t1 == t2 or t1 == t3 or t2 == t3:
    print('Triângulo Isósceles!')
else:
    print('Triângulo Escaleno!')