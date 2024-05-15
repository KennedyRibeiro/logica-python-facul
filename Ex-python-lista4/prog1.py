cont = 5
valores = [""] * cont

i = 0
par = 0
impar = 0

while i < cont:
    numeros = int(input("Digite um número: "))
    passarinho = numeros % 2
    
    if passarinho == 0:
        print("Ele é par!")
        par += 1
    else:
        print("Ele é impar!")
        impar += 1
        


    i += 1

print("A quantidade de números par é: ", par)
print("A quantidade de números impar é: ", impar)

    