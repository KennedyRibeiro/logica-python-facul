#Desenvolva um algoritmo para calcular a altura do cilindro, dada por V / (Pi R2), onde R é o raio, V é o volume e Pi uma constante equivalente a 3,1416. Os valores R e V deverão ser fornecidos pelo usuário#

PI = 3.14
v = float(input("Qual é o valor de v? "))
r = float(input("Qual é o valor de r? "))
altura = v / (PI * r ** 2)
print("A altura é : ", altura)