# Passo 1: Criar a lista com o gabarito oficial
GABARITO = ["B", "C", "A", "E", "D"]
def verificar_desempenho():
    respostas_usuario = []
    acertos = 0
    print("--- Sistema de Correção de Provas ---")
    for i in range(5):
        resposta = input(f"Digite a resposta da questão {i + 1}: ").strip().upper()
        respostas_usuario.append(resposta)
    for i in range(5):
        if respostas_usuario[i] == GABARITO[i]:
            acertos += 1
    print("\n" + "="*20)
    print(f"Total de acertos: {acertos} de 5")
    print(f"Gabarito oficial: {GABARITO}")
    print(f"Suas respostas:   {respostas_usuario}")
    print("="*20)
verificar_desempenho()