#Construa um algoritmo que seja capaz de construir qual dentre os seguintes animais foi escolhido, através de perguntas e respostas. Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.#



print("============================================================")
print("==================Bem-Vindo ao Zoológico====================")
print("============================================================")

code = int(input("1-Mamíferos, 2-Aves, 3-Répteis"))

if code == 1:
    code = int(input("1-Quadrúpedes, 2-Bípedes, 3-Voadores, 4-Aquáticos"))
    if code == 1:
        code = int(input("1-Carnívoros, 2-Herbívoros"))
        if code == 1:
            print("O Animal é um leão")
        else:
            print("O Animal é um cavalo")
    elif code == 2:
        code = int(input("1-Onívoros, 2-Frutiferos"))
        if code == 1:
            print("O Animal é um Homem")
        else:
            print("O Animal é um Macaco")
    elif code == 3:
        print("O Animal é um Morcego")
    else:
        print("O Animal é uma Baleia")
elif code == 2:
    code = int(input("1-Não Voadores, 2-Nadadores, 3-De rapina"))
    if code == 1:
        code = int(input("1-Tropical, 2-Polar"))
        if code == 1:
            print("O Animal é um Avestruz")
        else:
            print("O Animal é um Pinguim")
    elif code == 2:
        print("O Animal é um Pato")
    else:
        print("O Animal é uma Águia")
elif code == 3:
    code = int(input("1-Com casco, 2-Carnívoros, 3-Sem Patas"))
    if code == 1:
        print("O Animal é uma Tartaruga")
    elif code == 2:
        print("O Animal é um Crocodilo")
    else:
        print("O Animal é uma Cobra")
                




    