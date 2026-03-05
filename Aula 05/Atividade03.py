# Atividade 03

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

if x == y == z:
    print("Objeto Equilátero")
elif x == y or z == y or z == x:
    print("Objeto Isosceles")
else:
    print("Escaleno")
    