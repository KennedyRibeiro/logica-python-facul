#– Desenvolva um algoritmo para calcular a função F(x,y) = 2x + 2y2, em um domínio real. Os valores X e Y deverão ser fornecidos pelo usuário#

x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))
f = 2 * x + 2 * y ** 2
print("O resultado é: ", f)