# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, prepare um algoritmo para gerar o número H. O número N é fornecido pelo usuário.


h = 0 
num = 1

cont = 1

while cont <= 3:
    den = int(input("Qual o valor do denominador? "))
    h = num / den
    
    print("O valor de H é: ", h)
    
    cont += 1
    

