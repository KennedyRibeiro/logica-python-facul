
print('------Bem-vindos a loja de marmitas do Kennedy Ribeiro------')
print('-' * 26 +'Cardápio'+ '-' * 26 )
print('-' * 60)
print('----| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |---')
print('----|    P    |      R$ 16.00      |      R$ 15.00      |---')
print('----|    M    |      R$ 18.00      |      R$ 17.00      |---')
print('----|    G    |      R$ 22.00      |      R$ 21.00      |---')

sabor = input('Entre com o sabor desejado (BA/FF): ')
tamanho = input('Entre com o tamanho desejado (P/M/G): ')

acumulador = 0

if sabor == 'BA' or sabor == 'FF':
    if tamanho == 'P':
        if sabor == 'BA':
            acumulador += 1
            print('Você pediu um bife Acebolado no tamanho P: R$ 16.00')
        elif sabor == 'FF':
            acumulador += 1
            print('Você pediu um filé de frango no tamanho P: R$ 15.00')
    elif tamanho == 'M':
        if sabor == 'BA':
            acumulador += 1
            print('Você pediu um bife Acebolado no tamanho M: R$ 18.00')
        elif sabor == 'FF':
            acumulador += 1
            print('Você pediu um filé de frango no tamanho M: R$ 17.00')
    elif tamanho == 'G':
        if sabor == 'BA':
            acumulador += 1
            print('Você pediu um bife Acebolado no tamanho G: R$ 22.00')
        elif sabor == 'FF':
            acumulador += 1
            print('Você pediu um filé de frango no tamanho G: R$ 21.00')
    else:
        print('Tamanho inválido. Tente novamente')
else:
    print('Sabor inválido. Tente novamente')