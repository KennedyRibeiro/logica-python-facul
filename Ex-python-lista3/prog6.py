h = 0
sinal = 1
num = 1

while num <= 10:
    h = h + sinal * (num / num ** 2)
    sinal = sinal * -1
    num = sinal + 1
    
print("O valor de H é: ", h)
