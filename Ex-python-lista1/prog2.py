#Desenvolva um algoritmo para calcular a expressão S = (A + B) / (A – B). Os valores A e B deverão ser fornecidos pelo usuário.#


a = float(input("Qual o valor de A: "))
b = float(input("Qual o valor de B: "))
resultado = (a + b)/(a - b)
print("O resultado é: ", resultado)