'''
    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
    que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

metros = int(input("Informe o tamanho em metros quadrados: "))

litros = metros / 3

valor = 80.0
latas = 18

qtd_latas = int(litros / latas)

if (qtd_latas % 3 != 0):
    qtd_latas += 1
    
preco = qtd_latas * valor

if (qtd_latas <= 1):
    print(f"O valor a ser pago R$ 80.00\nVocê vai precisar de apenas 1 lata de 18L")
else:
    print(f"O valor a ser pago R$ {preco:.2f}\nVocê vai precisar de {qtd_latas} latas de 18L")