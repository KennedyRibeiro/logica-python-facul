# Faça um algoritmo que receba a quantidade de peças vendidas por cada vendedor e armazene essasquantidades em um vetor. Receba também o preço da peça vendida de cada vendedor e armazene esses preçosem outro vetor. Existem apenas 10 vendedores, e cada vendedor pode vender apenas um tipo de peça, isto é, paracada vendedor existe apenas um preço. Calcule e imprima a quantidade total de peças vendidas por todosvendedores e, para cada vendedor, calcule e imprima o valor da venda, isto é, a quantidade de peças * preço da peça.

vendedores = 3

qtdPeca = [""] * vendedores
precoPeca = [""] * vendedores

i = 0 

while i < vendedores:
    qtdPeca[i] = int(input("Olá vendedor! quantas peças você vendeu ? "))
    precoPeca[i] = float(input("Qual foi o preço da peça ? "))

    i += 1


i = 0
soma = 0

while i < vendedores:
    soma += qtdPeca[i]

    i += 1

i = 0

while i < vendedores:
    valorVenda = qtdPeca[i] * precoPeca[i]

    print("Total de vendas deste vendedor", i ,"é: R$",valorVenda)
    i += 1

print("A quantidade e peças vendidas por todos os vendedores: ", soma, "unidades")