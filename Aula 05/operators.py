# Demonstração de condicionais e operadores
tempo = input("Qual a condição metereológica?")
reserva = input("Tem algum dinheiro na conta?")

if tempo == "sol" and reserva == "sim":
    print("Dá para ir á praia!")

    if not tempo == "sol" and reserva == "sim":
        print("Comprar pizza e assistir Netflix!")

if tempo == "sol" or reserva == "não":
    print("vamos passear de bicicleta!")

    