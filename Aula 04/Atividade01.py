# Atividade 01

print("Digite o seu saldo atual:")
SALDO = float(input())

print("Digite o valor do produto desejado")
VALOR = float(input())

if SALDO >= VALOR:
    print("Parabéns pela compra!")
else:
    print("Você não possui saldo suficiente para realizar esta compra")
    print("Você não poderá realizar está compra, sinto muito...")
    