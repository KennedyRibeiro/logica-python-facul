#Construa um algoritmo que seja capaz de construir qual dentre os seguintes animais foi escolhido, através de perguntas e respostas. Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.#



print("============================================================")
print("==================Bem-Vindo ao Zoológico====================")
print("============================================================")
opcao = int(input("Escolha uma opção para chegar até o animal. Opção 1, 2 ou 3. "))
print("============================================================")

if opcao == 1:
    print("Mamiferos.")
    opcao = int(input("Agora para proseguir, escolha uma opção de 1 à 4. "))
else:
    if opcao >= 1 and opcao <= 4:
        print("")
    