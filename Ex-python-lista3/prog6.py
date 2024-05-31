# – Elabore um algoritmo que determine o valor de S, em que: S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 ... – 10/100.

h = 0
sinal = 1
num = 1

while num <= 10:
    h = h + sinal * (num / num ** 2)
    sinal = sinal * -1
    num = sinal + 1

print("O valor de H é: ", h)