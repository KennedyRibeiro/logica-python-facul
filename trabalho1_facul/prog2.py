
# Exibe o painel do cardapio e o nome da minha loja
print('------Bem-vindos a loja de marmitas do Kennedy Ribeiro------')
print('-' * 26 +'Cardápio'+ '-' * 26 )
print('-' * 60)
print('----| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |---')
print('----|    P    |      R$ 16.00      |      R$ 15.00      |---')
print('----|    M    |      R$ 18.00      |      R$ 17.00      |---')
print('----|    G    |      R$ 22.00      |      R$ 21.00      |---')

# Inicializa o acumulador de pedidos
acumulador = 0

# Loop para permitir múltiplos pedidos
while True:
    # Solicita o sabor do pedido
    sabor = input('Entre com o sabor desejado (BA/FF): ').upper() #.upper tudo digitado fica maiusculo
    
    # Valida o sabor
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido. Tente novamente.')
        continue  # Pula para o início do loop para nova tentativa
    
    # Solicita o tamanho do pedido
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
    
    # Valida o tamanho
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente.')
        continue  # Pula para o início do loop para nova tentativa
    
    # Processa o pedido com base no sabor e tamanho
    if sabor == 'BA':
        if tamanho == 'P':
            valor = 16.00
            print(f'Você pediu um bife Acebolado no tamanho P: R$ {valor:.2f}')
        elif tamanho == 'M':
            valor = 18.00
            print(f'Você pediu um bife Acebolado no tamanho M: R$ {valor:.2f}')
        elif tamanho == 'G':
            valor = 22.00
            print(f'Você pediu um bife Acebolado no tamanho G: R$ {valor:.2f}')
    elif sabor == 'FF':
        if tamanho == 'P':
            valor = 15.00
            print(f'Você pediu um filé de frango no tamanho P: R$ {valor:.2f}')
        elif tamanho == 'M':
            valor = 17.00
            print(f'Você pediu um filé de frango no tamanho M: R$ {valor:.2f}')
        elif tamanho == 'G':
            valor = 21.00
            print(f'Você pediu um filé de frango no tamanho G: R$ {valor:.2f}')
    
    # Adiciona o valor do pedido ao acumulador
    acumulador += valor
    
    # Pergunta se o usuário deseja pedir mais alguma coisa
    resposta = input('Deseja mais alguma coisa? (sim/não): ').strip().lower() #strip remove os espaços em branco
    if resposta != 'sim':
        break  # Sai do loop se a resposta for diferente de 'sim'

# Exibe o total acumulado dos pedidos
print(f'O valor total dos pedidos é: R$ {acumulador:.2f}')