#Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:#


idade = int(input("Qual é a sua idade nadador? "))

if idade >= 5 and idade <= 7:
    print("Infantil A")
else:
    if idade >= 8 and idade <= 10:
        print("Infantil B")
    else:
        if idade >= 11 and idade <= 13:
            print("Juvenil A")
        else:
            if idade >= 14 and idade <= 17:
                print("Juvenil B")
            else:
                if idade >= 18:
                    print("Adulto")
                else:
                    print("Categoria Invalida!")