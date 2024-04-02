#Desenvolva um algoritmo para calcular o volume de um cilindro, dado por Pi R2 H, onde R é o raio, H é a altura e Pi uma constante equivalente a 3,1416. Os valores de R e H deverão ser fornecidos pelo usuário#


PI = 3.14
r = float(input("Qual o valor de r? "))
h = float(input("Qual o valor de h? "))
valor = PI * r ** 2 * h
print("O valor é: ", valor)