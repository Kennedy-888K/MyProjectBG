# Atividade 03 MEGASENA
numeros = []

while len(numeros) < 6:
    n = int(input("Digite um número: "))

    if n in numeros:
        print("Número repetido, digite outro.")
    else:
        numeros.append(n)

print("Números escolhidos:", numeros)