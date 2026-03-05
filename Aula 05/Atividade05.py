# Atividade 05 

servico = input("O serviço foi prestado corretamente? (sim/nao): ")

if servico == "sim":
    print("Avalie o serviço:")
    print("1 - péssimo")
    print("2 - ruim")
    print("3 - razoável")
    print("4 - bom")
    print("5 - ótimo")
    
    nota = int(input("Digite a nota (1 a 5): "))
    
    if nota >= 1 and nota <= 5:
        print("Nota registrada:", nota)
    else:
        print("Nota inválida.")
        
elif servico == "nao":
    nota = 0
    print("Nota registrada:", nota)
    reclamacao = input("Descreva sua reclamação: ")
    print("Reclamação registrada com sucesso.")
    
else:
    print("Resposta inválida.")