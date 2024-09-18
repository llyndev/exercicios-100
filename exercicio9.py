# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 

fahrenheit = float(input("Digite os graus em Fahrenheit: "))

celsius = 5 * ((fahrenheit-32)/9)

print(f"{fahrenheit}°F to {celsius:.1f}°C")