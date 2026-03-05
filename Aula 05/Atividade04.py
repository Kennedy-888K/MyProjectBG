# Atividade 04

funcao = input("Digite sua função em campo: ")

if funcao in ["goleiro", "zagueiro", "lateral"]:
    print("Você é um jogador defensivo")

elif funcao in ["ala", "volante", "meia"]:
    print("Você é meio campista")

elif funcao in ["ponta", "centroavante", "atacante"]:
    print("Você é um jogador de ataque")

else:
    print("Teimoso!")
