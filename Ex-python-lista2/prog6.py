# Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação. Utilize a seguinte tabela como referência:

#Código    Classificação 
#============================================= 
#1 Alimento não-perecível 
#2, 3 e 4    Alimento perecível 
#5 ou 6    Vestuário 
#7 Higiene pessoal 
#8 até 15    Limpeza e utensílios domésticos 
#Qualquer outro código  Inválido 
 
id = int(input("Qual é o identificador do produto? "))

if id == 1:
    print("Alimento não perecível")
else:
    if id == 2 or id == 3 or id == 4:
        print("Alimento perecível")
    else:
        if id == 5 or id == 6:
            print("Vestuário")
        else:
            if id == 7:
                print("Higiene pessoal")
            else:
                if id >= 8 and id <= 15:
                    print("Limpeza e utensílios domésticos")
                else:
                    print("Código inválido!")
 
 
 
 
 
 
 
