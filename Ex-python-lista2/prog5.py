#Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também, verifique e mostre se ela já tem idade para votar (16 anos ou mais) e para conseguir a carteira de habilitação (18 anos ou mais). 


ano_nasc = int(input("Qual o seu ano de nascimento? "))
ano_atual = int(input("Qual o ano atual? "))

idade = ano_atual - ano_nasc

if idade >= 18:
    print("Você já pode tirar sua CNH, e votar. Você tem : ", idade)
if idade >= 16 and idade < 18:
    print("Você pode apenas votar!", idade)
else:
    print("Você não pode votar ainda e nem CNH! Você tem apenas: ", idade)

