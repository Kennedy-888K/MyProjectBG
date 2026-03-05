# Demonstração de operadores lógicos em condicionais...
print("O que você vai fazer amanhã de manhã?")
print("dormir / estudar / planejar")
MANHA = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if MANHA == "dormir":
    print("Você está desperdiçando o seu dia!")
if TARDE == "jogar":
    print("Você está desperdiçando o seu dia!")

if MANHA == "estudar":
    print("Que bom! Você irá se aperfeiçoar!")
if TARDE == "treinar":
    print("Que bom! Você irá se aperfeiçoar!")

if MANHA == "planejar":
    if TARDE == "trabalhar":
        print("Para trabalhar melhor, devo planejar!")

print("Tenha um bom dia!")