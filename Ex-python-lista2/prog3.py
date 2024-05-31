#Desenvolva um algoritmo que calcule as raízes de uma equação do 2o. grau, na forma Ax2 + Bx + C, levando em consideração a existência de raízes reais.#

from math import sqrt

a = float(input("Qual o valor de A?"))
b = float(input("Qual o valor de B?"))
c = float(input("Qual o valor de C?"))

if a == 0:
    print("Coeficiente A inválido!")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Delta inválido - Negativo")
    else:
        raiz1 = (- b + sqrt(delta)) / (2 * a)
        raiz2 = (- b - sqrt(delta)) / (2 * a)
        print(raiz1, raiz2)