#Desenvolva um algoritmo para calcular o troco a ser devolvido a um cliente. Deve ser lido (fornecido pelo usuário) o valor a ser pago e o valor dado pelo cliente.#

custo = float(input("Qual o do produto? "))
valorDado = float(input("Qual o valor dado? "))
troco = valorDado - custo
print("O valor do troco é de R$",troco)
