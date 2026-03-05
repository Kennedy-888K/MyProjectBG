# Eis, as condições para o estudante ser aprovado:
# Nota: igual ou acima de 6, Presença: igual ou acima de 75%
# Se uma das condições não forem satisfeita, recuperação.
# Se nenhuma das condições não forem satisfeitas, reprovado.

nota = int(input("Digite a nota: "))
presença = int(input("Digite a presença: "))

if nota >= 6 and presença >= 75:
    print("Aprovado")
elif nota < 6 and presença < 75:
    print("Reprovado!")
else:
    print("Recuperação!")
    
