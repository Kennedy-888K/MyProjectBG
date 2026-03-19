# Atividade 03
def mostrar(nome, cidade):
    if cidade == "Rio de Janeiro":
        print(f"{nome} - Seja Bem-vindo à Cidade Maravilhosa")
    else:
        print(f"{nome} - {cidade}")

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

mostrar(nome, cidade)