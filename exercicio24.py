# Faça um Programa que leia três números e mostre o maior e o menor deles. 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"O maior valor digitado: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior valor digitado: {n2}")
elif n3 > n1 and n3 > n2:
    print(f"O maior valor digitado: {n3}")
else:
    print("Invalido")

if n1 < n2 and n1 < n3:
    print(f"O menor valor digitado: {n1}")
elif n2 < n1 and n3 < n1:
    print(f"O menor valor digitado: {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O menor valor digitado: {n3}")
else:
    print("Invalido")