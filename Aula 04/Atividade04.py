# Atividade 04

titulo = input("Digite o nome do filme ou série: ")
nota = int(input("Dê uma nota de 1 a 5: "))

match nota:
    case 1:
        print("Você avaliou como: Péssimo")
        motivo = input("Por que achou tão ruim? ")
        print("Entendido. Crítica registrada.")
        
    case 2:
        print("Você avaliou como: Ruim")
        motivo = input("Por que não gostou? ")
        print("Entendido. Crítica registrada.")
        
    case 3:
        print("Você avaliou como: Razoável")
        
    case 4:
        print("Você avaliou como: Bom")
        
    case 5:
        print("Você avaliou como: Ótimo")
        
    case _:
        print("Nota inválida! Digite um valor entre 1 e 5.")