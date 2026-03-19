# Atividade 01

def programas_infantis():
    print("Programas infantis:")
    print("- Peppa Pig")
    print("- Bob Esponja")
    print("- Dora Aventureira")


def lista_carros():
    print("Lista de carros e preços:")
    print("- Gol: R$ 40.000")
    print("- Onix: R$ 60.000")
    print("- Corolla: R$ 120.000")


idade = int(input("Digite sua idade: "))

if idade < 18:
    programas_infantis()
else:
    lista_carros()