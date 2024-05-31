# Em uma eleição presidencial, existem quatro candidatos. Os votos são informados através de código. Os dados utilizados para a escrutinagem obedecem à seguinte codificação:

canditado1 = 0
canditado2 = 0
canditado3 = 0
canditado4 = 0
nulo = 0
branco = 0

voto = 999

while voto > 0:
    voto = int(input("Seu voto vai para qual candidato ? 1, 2, 3, nulo5 ou branco6? "))
    if voto == 1:
        canditado1 += 1
    elif voto == 2:
        canditado2 += 1
    elif voto == 3:
        canditado3 += 1
    elif voto == 4:
        canditado4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    elif voto != 1 and voto != 2 and voto != 3 and voto != 4 and voto != 5 and voto != 6:
        print("Voto inválido! você só pode votar em canditado de 1 à 4 ou nulo5 e branco6!!")
    
print("Canditado 1, total: ",canditado1)
print("Canditado 2, total: ",canditado2)
print("Canditado 3, total: ",canditado3)
print("Canditado 4, total: ",canditado4)
print("Nulos total: ",nulo)
print("Brancos total: ",branco)

total = canditado1 + canditado2 + canditado3 + canditado4 + nulo + branco

percentualNulo = (total * nulo) / 100
percentualBranco = (total * branco) / 100

print("o percentual de votos nulos é : ",percentualNulo,"%")
print("o percentual de votos em branco é : ",percentualBranco,"%")