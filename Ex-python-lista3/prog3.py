
print("Fahrenheit | Celcius")
print("----------|---------")

fahrenheit = float(input("Qual o valor de fahrenheit? 50 á 150 "))

while fahrenheit >= 50 and fahrenheit <= 150:
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit," | ", celsius)

