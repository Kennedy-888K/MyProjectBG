# Demo
tabuada = []
for X in range (1, 10):
    linhas = []
    for Y in range(1, 10):
        linhas.append(X * Y)
    tabuada.append(linhas)
for tabela in tabuada:
    print(tabela)
