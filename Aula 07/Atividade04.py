#Atividade 04
valor = int(input("Digite o valor: "))

notas200 = valor // 200
valor = valor % 200

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2
valor = valor % 2
print("Notas de 200:", notas200)
print("Notas de 100:", notas100)
print("Notas de 50:", notas50)
print("Notas de 20:", notas20)
print("Notas de 10:", notas10)
print("Notas de 5:", notas5)
print("Notas de 2:", notas2)