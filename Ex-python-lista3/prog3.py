# A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = 5/9(F – 32). Escreva um algoritmo que calcule e mostre uma tabela de graus centígrados em função de graus Fahrenheit que variem de 50 a 150 de 1 em 1.

print("Fahrenheit | Celcius")
print("----------|---------")

fahrenheit = float(input("Qual o valor de fahrenheit? 50 á 150 "))

while fahrenheit >= 50 and fahrenheit <= 150:
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit," | ", celsius)