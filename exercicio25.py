# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato. 

v1 = float(input("Informe o preço do primeiro produto: "))
v2 = float(input("Informe o preço do segundo produto: "))
v3 = float(input("Informe o preço do terceiro produto: "))

if v1 < v2 and v1 < v3:
    print(f"Compre o produto no valor de R$ {v1:.2f}")
elif v2 < v1 and v2 < v3:
    print(f"Compre o produto no valor de R$ {v2:.2f}")
elif v3 < v1 and v3 < v2:
    print(f"Compre o produto no valor de R$ {v3:.2f}")
else:
    print("Digite valores validos")