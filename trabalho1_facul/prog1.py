
# Exibe uma mensagem de boas-vindas ao usuário
print('Bem-Vindo a loja do Kennedy Henrique Ribeiro')

# Solicita ao usuário o valor do pedido e a quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeDeParcelas = int(input("Entre com a quantidade de parcelas: "))

# Verifica a quantidade de parcelas e aplica a taxa de juros correspondente e calcula o valor de cada parcela, incluindo juros

if quantidadeDeParcelas < 4:
    juros = 0
    valorDaParcela = valorDoPedido * (1 + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6:
    juros = 0.04
    valorDaParcela = valorDoPedido * (1 + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas < 9:
    juros = 0.08
    valorDaParcela = valorDoPedido * (1 + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13:
    juros = 0.16
    valorDaParcela = valorDoPedido * (1 + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
else:
    juros = 0.32
    valorDaParcela = valorDoPedido * (1 + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas

# Exibe o valor da parcela e o valor total parcelado, formatados com duas casas decimais
print(f'O valor das parcelas é de: R$ {valorDaParcela:.2f}')
print(f'O valor total parcelado é de: R$ {valorTotalParcelado:.2f}')