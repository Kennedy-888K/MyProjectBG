# Atividade 03

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc > 25:
    categoria = "acima"
elif imc < 18:
    categoria = "abaixo"
else:
    categoria = "ok"

match categoria:
    case "acima":
        print("Acima do peso ideal")
    case "abaixo":
        print("Abaixo do peso ideal")
    case "ok":
        print("O seu peso está OK")

print("Seu IMC foi:", round(imc, 2))