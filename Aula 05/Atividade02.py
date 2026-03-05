# Atividade 02

# Recebendo os 3 valores
x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
z = float(input("Digite o terceiro valor: "))

if x>y and y>z:
    print("Está em Decrescente!")
if x<y and y<z:
    print("Está em Crescente")
else:
    print("Eles estão misturados")
    