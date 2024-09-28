# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for i in range(3):
    n = int(input("Digite um número: "))
    numeros.append(n)
    
numeros.sort(reverse=True)
print(numeros)
    