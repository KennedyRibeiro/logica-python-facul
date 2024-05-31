#Desenvolva um algoritmo para calcular a expressão S = A + B – C * AC / B. Os valores A, B e C deverão ser fornecidos pelo usuário#

A = float(input("Qual o valor de A: "))
B = float(input("Qual o valor de B: "))
C = float(input("Qual o valor de C: "))
resultado = A + B - C * A ** C / B
print("O resultado é ", resultado)