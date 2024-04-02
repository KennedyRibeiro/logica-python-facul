#Desenvolva um algoritmo para calcular o valor das raízes de uma equação do 2º grau (Ax2 + Bx + C), sabendo-se que: Delta = B2 – 4AC Raízes = (- B + SQRT(Delta)) / (2A), (- B - SQRT(Delta)) / (2A)Os valores A, B e C deverão ser fornecidos pelo usuário. SQRT() – Função para cálculo de raiz quadrada.#

from math import sqrt
a = float(input("Qual o valor de A?"))
b = float(input("Qual o valor de B?"))
c = float(input("Qual o valor de C?"))


delta = b ^ 2 - 4 * a * c
raiz1 = (-b + sqrt (delta)) / (2 * a)
raiz2 = (-b - sqrt (delta)) / (2 * a)
print("raiz1 é: ", raiz1, "raiz2 é: ", raiz2)




