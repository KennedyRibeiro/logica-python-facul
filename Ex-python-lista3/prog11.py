# Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto Felisberto tem 1,10 metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Felisberto seja maior que Anacleto.

anaCleto = 150
felisberto = 110

cont = 0

while felisberto < anaCleto:
    anaCleto += 2
    felisberto += 3
    
    cont = cont + 1

print("Felisberto precisou de ",cont,"° anos Para chegar na altura de anaCleto")