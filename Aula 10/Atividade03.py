time = []

for i in range(11):
    camisa = input("Número da camisa: ")
    nome = input("Nome do jogador: ")
    posicao = input("Posição: ")

    time.append([camisa, nome, posicao])

print("\nTitulares:")
for jogador in time:
    print(jogador)

for i in range(3):
    print("\nSubstituição", i+1)
    pos = int(input("Qual jogador sai? (0 a 10): "))

    camisa = input("Número da camisa do suplente: ")
    nome = input("Nome do suplente: ")
    posicao = input("Posição: ")

    time[pos] = [camisa, nome, posicao]

print("\nTime atualizado:")
for jogador in time:
    print(jogador)