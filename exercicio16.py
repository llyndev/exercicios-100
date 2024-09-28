'''
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
    que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
'''

metros = int(input("Informe o tamanho em metros quadrados: "))

latas = metros / 6

galoes = metros / 3.6

valor_galoes = 25.0

valor_latas = 80.0

litros1 = 18.0

litros2 = 3.6

qtd_latas = int(latas / litros1)

qtd_galoes = int(galoes / litros2)

if qtd_latas % 3 != 0:
    qtd_latas += 1  
    
preco_latas = qtd_latas * valor_latas

if qtd_latas <= 1:
    print(f"O valor a ser pago R$ 80.00\nVocê vai precisar de apenas 1 lata de 18L")
else:
    print(f"O valor a ser pago em latas R$ {preco_latas:.2f}\nVocê vai precisar de {qtd_latas} latas de 18L\n")

    
if qtd_galoes % 3.6 != 0:
    qtd_galoes += 1

preco_galoes = qtd_galoes * valor_galoes

    
print('')

if qtd_galoes <= 1:
    print(f"O valor a ser pago R$ 25.00\nVocê vai precisar de apenas 1 galão de 3.6L")
else:
    print(f"O valor a ser pago em galões R$ {preco_galoes:.2f}\nVocê vai precisar de {qtd_galoes} galões de 3.6L")