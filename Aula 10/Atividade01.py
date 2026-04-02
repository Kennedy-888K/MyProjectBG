print("Digite os valores da matriz 2x2")

matriz = [[0, 0],
          [0, 0]]

soma = 0

for x in range(0, 2):
    for y in range(0, 2):
        matriz[x][y] = int(input("Digite um valor: "))
        soma = soma + matriz[x][y]

media = soma / 4

print("Matriz digitada:")
for linha in matriz:
    print(linha)

print("Soma =", soma)
print("Média =", media)