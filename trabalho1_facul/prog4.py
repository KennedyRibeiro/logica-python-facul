# Exibe a mensagem de boas-vindas com o nome do desenvolvedor
print("-----------------------------------------")
print("Bem-vindos à empresa do Kennedy Ribeiro")
print("-----------------------------------------")

# lista e variavel
lista_funcionarios = []
id_global = 4971058  

# função de cadastrar o usuario
def cadastrar_funcionario(id):
    print("-----------------------------------------")
    print("------- MENU CADASTRAR FUNCIONARIO ------")
    print(id)
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

# função para consultar usuario
def consultar_funcionarios():
    while True:
        print("-----------------------------------------")
        print("------- MENU CONSULTAR FUNCIONARIO ------")
        print("1 - Consultar Todos os funcionários")
        print("2 - Consultar funcionário por Id")
        print("3 - Consultar funcionário por Setor")
        print("4 - Retornar ao menu")
        opcao = int(input("Escolha a opção desejada: "))

        if opcao == 1:
            print("\nTodos os Funcionários:")
            print("")
            for funcionario in lista_funcionarios:
                print('ID: ',funcionario['id'])
                print('Nome: ',funcionario['nome'])
                print('Setor: ',funcionario['setor'])
                print('Salário: R$',funcionario['salario'])
                print("")

        elif opcao == 2:
            id_consulta = int(input("Digite o Id do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print("----------------------")
                    print('ID: ',funcionario['id'])
                    print('Nome: ',funcionario['nome'])
                    print('Setor: ',funcionario['setor'])
                    print('Salário: R$',funcionario['salario'])
                    print("")
                    encontrado = True
                    break
            if not encontrado:
                print("Id não encontrado.")

        elif opcao == 3:
            setor_consulta = input("Digite o setor do(s) funcionário(s): ")
            encontrados = [funcionario for funcionario in lista_funcionarios if funcionario['setor'] == setor_consulta]
            if encontrados:
                for funcionario in encontrados:
                    print("----------------------")
                    print('ID: ',funcionario['id'])
                    print('Nome: ',funcionario['nome'])
                    print('Setor: ',funcionario['setor'])
                    print('Salário: R$',funcionario['salario'])
                    print("")
            else:
                print("Nenhum funcionário encontrado neste setor.")

        elif opcao == 4:
            return

        else:
            print("Opção inválida.")

# função para remover o usuario
def remover_funcionario():
    while True:
        print("-----------------------------------------")
        print("------- MENU REMOVER FUNCIONARIO ------")
        id_remocao = int(input("Digite o Id do funcionário a ser removido: "))
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remocao:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário de Id {id_remocao} removido com sucesso.")
                return
        print("Id inválido.")

# loop do menu principal
while True:
    print("-----------------------------------------")
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