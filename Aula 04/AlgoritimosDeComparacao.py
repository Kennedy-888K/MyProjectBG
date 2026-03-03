# Demonstração do uso de IF/ELIF/ELSE
print("Digite a sua idade:")
IDADE = int(input())

if IDADE < 18:
    print("Você não é maior de idade!")
    print("Não poderá realizar operações bancárias!")
elif IDADE >= 65:
    print("Você já é aposentado!")
    print("Poderemos oferecer suporte técnico...")    
else:
    print("Você é maior de idade!")
    print("Portanto, poderá realizar a operação.")

print("Obrigado por escolher os nossos serviços!")

