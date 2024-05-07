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
        
    print(FirtCandidato, SecondCandidato, ThirdCandidato)

    