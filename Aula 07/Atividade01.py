# Atividade 01
numero = int(input("Digite um número entre 0 e 25: "))

if numero < 0 or numero > 25:
    print("Número inválido! Digite um valor entre 0 e 25.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial = fatorial * i

    print("O fatorial de", numero, "é:", fatorial)


    