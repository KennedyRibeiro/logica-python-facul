#Desenvolva um algoritmo para calcular o preço médio do quilômetro rodado para uma distância percorrida (em Km) e um certo volume de combustível consumido (em litros). O valor do preço do litro de combustível, o quilômetro rodado e o volume consumido deverão ser fornecidos pelo usuário#


preco_litro = float(input("Qual o preço do litro do combustível?"))
km = float(input("Qual o KM rodado?"))
consumo = float(input("Qual o volume do combustível consumido?"))
preco_medio = (consumo / km) * preco_litro
print("O Preço médio gasto por litro é: ", preco_medio)