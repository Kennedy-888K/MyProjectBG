# Atividade 02

def jogo(usuario, computador):
    soma = usuario + computador

    if soma % 2 == 0:
        print("Soma =", soma)
        print("Usuário venceu! (Par)")
    else:
        print("Soma =", soma)
        print("Computador venceu! (Ímpar)")

usuario = int(input("Digite seu número: "))
computador = int(input("Digite o número do computador: "))

jogo(usuario, computador)