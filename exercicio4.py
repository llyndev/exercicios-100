# Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

aluno = input("Digite o nome do aluno: ")

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"A média do {aluno} é {media}")