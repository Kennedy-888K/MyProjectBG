# Atividade 01

time = input("Digite o time:")
classificação = int(input("Digite a classificação:"))

if classificação == 1:
    print("Campeão!")
elif classificação >= 7 and classificação <=12:
    print("Libertadores!")
else:
    print("Rebaixado!")
    