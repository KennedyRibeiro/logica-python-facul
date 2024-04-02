#Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado. #


id = int(input("Qual o código da forma de pagamento? "))

if id == 1:
    print("À vista em dinheiro ou cheque, recebe 10% de desconto.")
else:
    if id == 2:
        print("À vista no cartão de crédito, recebe 5% de desconto.")
    else:
        if id == 3:
            print("Em 2 vezes, preço normal de etiqueta sem juros.")
        else:
            if id == 4:
                print("Em 3 vezes, preço normal de etiqueta com mais juros de 10% ")
            else:
                print("Código de pagamento invalido!")