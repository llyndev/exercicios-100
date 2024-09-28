# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = {"a", "e", "i", "o", "u"}

letra = input("Digite uma letra: ").upper()

if letra in vogal:
    print(f"A letra: {letra} é uma vogal.")
else:
    print(f"A letra: {letra} é consoante.")