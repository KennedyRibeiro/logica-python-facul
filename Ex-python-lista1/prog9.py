#Desenvolva um algoritmo para calcular (converter) graus Farenheit (F) em graus Centígrados (C) utilizando a seguinte fórmula: C = 5 (F – 32) / 9. O valor F deverá ser lido.#

f = float(input("Qual o valor de f?"))
c = 5 * (f - 32) / 9
print("O valor de centigrados é: ", c)