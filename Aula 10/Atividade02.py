matriz = []
numeros = []

for x in range(3):
    linha = []
    for y in range(3):
        valor = int(input("Digite um número de 1 a 9: "))

        while valor in numeros:
            print("Número repetido!")
            valor = int(input("Digite outro número: "))

        linha.append(valor)
        numeros.append(valor)

    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

for linha in matriz:
    print("Soma da linha =", sum(linha))

for y in range(3):
    print("Soma da coluna =", matriz[0][y] + matriz[1][y] + matriz[2][y])

diagonal1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
diagonal2 = matriz[0][2] + matriz[1][1] + matriz[2][0]

print("Diagonal 1 =", diagonal1)
print("Diagonal 2 =", diagonal2)