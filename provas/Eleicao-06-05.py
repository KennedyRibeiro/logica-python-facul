FirtCandidato = 0
SecondCandidato = 0
ThirdCandidato = 0

voto = 999

while voto > 0:
    voto = int(input("Vote em seu canditado: 1, 2, 3 ou 0 para sair. "))
    if voto == 1:
        print("Você votou no candidato número 1! ")
        FirtCandidato += 1
    elif voto == 2:
        print("Você votou no candidato número 2! ")
        SecondCandidato = SecondCandidato + 1
    elif voto == 3:
        print("Você votou no candidato número 3!")
        ThirdCandidato = ThirdCandidato + 1
    elif voto != 1 and voto != 2 and voto != 3:
        print("Você não pode votar nulo ou em branco! Somente em um dos candidatos: 1, 2 ou 3")
        
    print(FirtCandidato, SecondCandidato, ThirdCandidato)

totalVotos = FirtCandidato + SecondCandidato + ThirdCandidato

percentual1 = (totalVotos * FirtCandidato) / 100
percentual2 = (totalVotos * SecondCandidato) / 100
percentual3 = (totalVotos * ThirdCandidato) / 100

print("O Percentual de votos de cada candidato: ")
print("Candidato 1: ",percentual1,"%")
print("Candidato 2: ",percentual2,"%")
print("Candidato 3: ",percentual3,"%")


if FirtCandidato > SecondCandidato and FirtCandidato > ThirdCandidato:
    print("O Candidato vencedor é o 1°!!")
elif SecondCandidato > FirtCandidato and SecondCandidato > ThirdCandidato:
    print("O Candidato vencedor é o 2°!!")
elif ThirdCandidato > FirtCandidato and ThirdCandidato > SecondCandidato:
    print("O Candidato vencedor é o 3°!!")


if FirtCandidato == SecondCandidato:
    print("O 1° candidato empatou com o 2°!!")
elif SecondCandidato == ThirdCandidato:
    print("O 2° candidato empatou com o 3°!!")
elif FirtCandidato == ThirdCandidato:
    print("O 1° candidato empatou com o 3°!!")





