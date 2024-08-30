
print("-----------------------------------------")
print("Bem-vindos à empresa do Kennedy Ribeiro")
print("-----------------------------------------")


lista_funcionarios = []
id_global = 4971058  


def cadastrar_funcionario(id):
    nome = input("Por favor entre com o nome do funcionário: ")
    setor = input("Por favor entre com o setor do funcionário: ")
    salario = float(input("Por favor entre com o salário do funcionário: "))

    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    lista_funcionarios.append(funcionario.copy())
    print(f"Funcionário {nome} cadastrado com sucesso!\n")


def consultar_funcionarios():
    while True:
        print("\nConsultar Funcionários:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("\nTodos os Funcionários:")
            for funcionario in lista_funcionarios:
                print(funcionario)

        elif opcao == 2:
            id_consulta = int(input("Digite o Id do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print("Id não encontrado.")

        elif opcao == 3:
            setor_consulta = input("Digite o setor: ")
            encontrados = [funcionario for funcionario in lista_funcionarios if funcionario['setor'] == setor_consulta]
            if encontrados:
                for funcionario in encontrados:
                    print(funcionario)
            else:
                print("Nenhum funcionário encontrado neste setor.")

        elif opcao == 4:
            return

        else:
            print("Opção inválida.")

# EXIGÊNCIA DE CÓDIGO 5 de 8
def remover_funcionario():
    while True:
        id_remocao = int(input("Digite o Id do funcionário a ser removido: "))
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remocao:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário de Id {id_remocao} removido com sucesso.")
                return
        print("Id inválido.")

# EXIGÊNCIA DE CÓDIGO 6 de 8
while True:
    print("------------- MENU PRINCIPAL ------------")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == 2:
        consultar_funcionarios()
    elif opcao == 3:
        remover_funcionario()
    elif opcao == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

# EXIGÊNCIAS DE SAÍDA DE CONSOLE
# 1. Nome completo já foi impresso no início do código.

# 2. Cadastro de 3 funcionários
id_global += 1
cadastrar_funcionario(id_global)  # Func. 1
id_global += 1
cadastrar_funcionario(id_global)  # Func. 2
id_global += 1
cadastrar_funcionario(id_global)  # Func. 3

# 3. Consultar Todos os funcionários
consultar_funcionarios()

# 4. Consultar por Id de um dos funcionários
consultar_funcionarios()

# 5. Consultar por setor (onde dois funcionários são do mesmo setor)
consultar_funcionarios()

# 6. Remover um funcionário e consultar todos novamente
remover_funcionario()
consultar_funcionarios()