# Exibe a mensagem de boas-vindas com o nome do desenvolvedor
print('Bem-Vindo a Fábrica de camisetas do Kennedy Ribeiro')

# Função para escolher o modelo da camiseta
def escolha_modelo():
    while True:
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Longa Com Estampa")
        print("MLE - Manga Longa Com Estampa")

        modelo = input('Entre com o modelo desejado: ').upper()

        # Retorna o valor correspondente ao modelo escolhido
        if modelo == 'MCS':
            return 1.80  
        elif modelo == 'MLS':
            return 2.10  
        elif modelo == 'MCE':
            return 2.90  
        elif modelo == 'MLE':
            return 3.20  
        else:
            print("Modelo inválido. Tente novamente.")

# Função para definir a quantidade de camisetas e aplicar o desconto, se aplicável
def num_camisetas():
    while True:
        try:
            num = int(input("Entre com o número de camisetas: "))

            # Verifica se o número de camisetas é válido
            if num <= 0 or num > 20000:
                print("Número de camisetas inválido. Tente novamente.")  
            elif num < 20:
                return num
            elif 20 <= num < 200:
                return num * 0.95  
            elif 200 <= num < 2000:
                return num * 0.93 
            elif 2000 <= num <= 20000:
                return num * 0.88
        except ValueError:  # Trata o erro caso o usuário não digite um número inteiro
            print("Entrada inválida. Digite um número inteiro.")

# Função para escolher a opção de frete
def frete():
    while True:
        try:
            opcao = int(input("Escolha o frete: \n1 - Transportadora - R$ 100.00\n2 - Sedex - R$ 200.00\n0 - Retirar na fábrica - R$ 0.00 \n"))

            # Retorna o valor correspondente à opção de frete escolhida
            if opcao == 1:
                return 100.00 
            elif opcao == 2:
                return 200.00  
            elif opcao == 0:
                return 0.00 
            else:
                print("Opção de frete inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite 1, 2 ou 0.")

# Código principal
if __name__ == "__main__":
    # chama as funções
    valor_modelo = escolha_modelo()
    num_camisetas_com_desconto = num_camisetas()
    valor_frete = frete()
    
    # Calcula o valor total do pedido
    total = (valor_modelo * num_camisetas_com_desconto) + valor_frete

    print(f"Total a pagar: R$ {total:.2f}")