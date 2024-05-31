# Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual a operação aritmética escolhida. #

n1 = int(input("Qual o valor do primeiro numero? "))
n2 = int(input("Qual o valor do segundo numero? "))
operacao = input("Qual a operação desejada? ")

if operacao == "adição":
    soma = n1 + n2
    print(soma)
else:
    if operacao == "subtração":
        sub = n1 - n2
        print(sub)
    else:
        if operacao == "multiplicação":
            mult = n1 * n2
            print(mult)
        else:
            if operacao == "divisão":
                div = n1 / n2
                print(div)
            else:
                print("Operação invalida! Somente: adição, subtração, multiplicação e divisão.")