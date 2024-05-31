#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
# Para homens: (72,7 * H) – 58 
# Para mulheres: (62,1 * H) – 44,7 

altura = float(input("Qual é a sua altura?"))
sexo = (input("Qual é o seu sexo?"))

if sexo == "masculino":
    peso_h = (72.7 * altura) - 58
    print("O seu peso ideal é: ", peso_h)
else:
    if sexo == "feminino":
        peso_m = (62.1 * altura) - 44.7
        print("O seu peso ideal é: ", peso_m)
    else:
        print("Sexo Inválido!")