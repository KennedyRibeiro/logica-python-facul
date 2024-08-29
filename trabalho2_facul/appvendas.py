
print("Bem-Vindo a Loja do Kennedy")
val_unit = float(input("Entre com o valor unitário do produto: "))
qtd_prod = int(input("Entre com a quantidade do produto: "))

valor = val_unit * qtd_prod

if valor < 2500:
    print("O valor sem desconto foi R$", valor)
    print("O Valor com desconto foi R$", valor)
else:
    if valor >= 2500 and valor < 6000:
        calc = (valor * 4) / 100
        c_desc = valor - calc
        print("O Valor sem desonto foi R$", valor)
        print("O Valor com desonto foi R$", c_desc,"(Desconto de 4%)")
    else:
        if valor >= 6000 and valor < 10000:
            calc = (valor * 6) / 100
            c_desc = valor - calc
            print("O Valor sem desonto foi R$", valor)
            print("O Valor com desonto foi R$", c_desc,"(Desconto de 6%)")
        else:
            if valor >= 10000:
                calc = (valor * 11) / 100
                c_desc = valor - calc
                print("O Valor sem desonto foi R$", valor)
                print("O Valor com desonto foi R$", c_desc,"(Desconto de 11%)")