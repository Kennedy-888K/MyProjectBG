# Atividade 02
# Cadastro do paciente

nome = input("Digite o nome do paciente: ")
data_nascimento = input("Digite a data de nascimento: ")
sexo = input("Digite o sexo: ")
diagnostico = input("Digite o diagnóstico: ")
estado = input("Digite o estado do paciente: ")
tratamento = input("Digite o tratamento: ")
data_liberacao = input("Digite a data de liberação: ")

print("\n--- FICHA DO PACIENTE ---")
print("Nome:", nome)
print("Data de nascimento:", data_nascimento)
print("Sexo:", sexo)
print("Diagnóstico:", diagnostico)
print("Estado:", estado)
print("Tratamento:", tratamento)
print("Data de liberação:", data_liberacao)

print("\nDeseja alterar algum dado? (s/n)")
resposta = input()

if resposta == "s":

    campo = input("Qual dado deseja alterar? (nome, diagnostico, estado, tratamento): ")

    if campo == "nome":
        nome = input("Digite o novo nome: ")

    elif campo == "diagnostico":
        diagnostico = input("Digite o novo diagnóstico: ")

    elif campo == "estado":
        estado = input("Digite o novo estado: ")

    elif campo == "tratamento":
        tratamento = input("Digite o novo tratamento: ")

print("\n--- FICHA ATUALIZADA ---")
print("Nome:", nome)
print("Data de nascimento:", data_nascimento)
print("Sexo:", sexo)
print("Diagnóstico:", diagnostico)
print("Estado:", estado)
print("Tratamento:", tratamento)
print("Data de liberação:", data_liberacao)