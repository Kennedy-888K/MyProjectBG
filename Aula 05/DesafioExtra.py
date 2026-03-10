# Cálculo da aposentadoria...
IDADE = int(input("Qual é a idade:"))
INSS = int(input("Qt. anos de contribuição:"))
INSALUBRE = int(input("Em condições insalubres (S/N)? "))

if INSALUBRE == "S":
    if INSS >= 25:
        print("aposentadoria especial")
    else:
        print(f"Faltam {25 - INSS} anos para se aposentar...")
else:
    if IDADE >= 65 and INSS >= 35:
        print("Aposentadoria Normal !")
    else:
        print("Falta atender aos requisitos...")
