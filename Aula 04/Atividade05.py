# Atividade 05

DiaDaSemana = input("Digite um dia da semana: ")
match DiaDaSemana:
    case "segunda":
        print("Estude 3 horas a mais")
    case "terça":
        print("Jogue bola 2 horas a menos")
    case "quarta":
        print("Faça horas extras no seu trabalho")
    case "quinta":
        print("Faça exercícios")
    case "sexta":
        print("Descanse o dia")
    case "sabado":
        print("Jogue basquete até cansar")
    case "domingo":
        print("Vá a Igreja")
    case _:
        print("Erro, Digite um dia da semana")
