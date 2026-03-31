def gerenciar_time():
    time = []

    print("--- Cadastro da Escalação Inicial ---")

    for i in range(11):
        print(f"\nJogador {i+1}:")
        nome = input("Nome: ")
        camisa = input("Número da camisa: ")
        time.append({"nome": nome, "camisa": camisa})

    
    print("\n--- Lista de Titulares ---")
    for jogador in sorted(time,key=lambda jogador: int(jogador['camisa'])):
        print(f"Camisa {jogador['camisa']} - {jogador['nome']}")


    print("\n--- Intervalo de Jogo ---")
    substituir = input("Deseja realizar substituições? (S/N): ").strip().upper()

    if substituir == 'S':
        for s in range(3):
            print(f"\nSubstituição {s+1} de 3:")
            num_sai = input("Número da camisa do jogador que SAI: ")
            
            
            encontrado = False
            for jogador in time:
                if jogador['camisa'] == num_sai:
                    print(f"Saindo: {jogador['nome']}")
                    novo_nome = input("Nome do jogador que ENTRA: ")
                    nova_camisa = input("Número da camisa do novo jogador: ")
                    
                    
                    jogador['nome'] = novo_nome
                    jogador['camisa'] = nova_camisa
                    encontrado = True
                    break
            
            if not encontrado:
                print("Jogador não encontrado com esse número.")

            if s < 2:
                mais_uma = input("Deseja fazer outra substituição? (S/N): ").strip().upper()
                if mais_uma != 'S':
                    break

    print("\n--- Escalação Final Atualizada ---")
    for jogador in sorted(time,key=lambda jogador: int(jogador['camisa'])):
        print(f"Camisa {jogador['camisa']} - {jogador['nome']}")

gerenciar_time()    