# Calcule o imposto de renda de um grupo de 10 contribuintes, considerando que os dados de cada contribuinte,número do CPF, número de dependentes e renda mensal são valores fornecidos pelo usuário. Para cadacontribuinte será feito um desconto de 5% do salário mínimo por dependente. Os valores da alíquota para cálculodo imposto são:

cont = 0
sal_min = float(input("Qual o sálario mínimo? "))

while cont <= 10:
    cpf = float(input("Qual o seu CPF? "))
    dependente = int(input("Quantas pessoas dependem de você? "))
    renda = float(input("Qual a sua renda mensal? "))

    renda_liq = renda - (sal_min * 0.05) * dependente

    if renda_liq <= 2 * sal_min:
        receba = 0
    elif renda_liq <= 3 * sal_min:
        receba = renda_liq * 0.05
    elif renda_liq <= 5 * sal_min:
        receba = renda_liq * 0.10
    elif renda_liq <= 7 * sal_min:
        receba = renda_liq * 0.15
    else:
        receba = renda_liq * 0.20
    
    print(cpf, receba)

    cont += 1