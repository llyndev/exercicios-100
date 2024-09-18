# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 

celsius = float(input("Digite os graus em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C to {fahrenheit:.1f}°F")