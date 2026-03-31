def lista_tarefas():
    tarefas = []
    print("--- Cadastro Inicial de Tarefas ---")
    for i in range(5):
        tarefa = input(f"Digite a descrição da {i+1}ª tarefa: ")
        tarefas.append(tarefa)
    print("\nSuas tarefas atuais:")
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t}")

    print("\n--- Verificação de Status ---")
    pergunta = input(f"A primeira tarefa ('{tarefas[0]}') já foi executada? (S/N): ").strip().upper()
    if pergunta == 'S':
        
        removida = tarefas.pop(0)
        print(f"Tarefa '{removida}' concluída e removida da lista.")
    else:
        print("A primeira tarefa permanece na lista.")
    opcao_nova = input("\nDeseja cadastrar uma nova tarefa? (S/N): ").strip().upper()
    if opcao_nova == 'S':
        nova_tarefa = input("Digite a descrição da nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Nova tarefa adicionada com sucesso!")

    print("\n--- Lista de Afazeres Atualizada ---")
    if len(tarefas) == 0:
        print("Sua lista está vazia.")
    else:
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
lista_tarefas()