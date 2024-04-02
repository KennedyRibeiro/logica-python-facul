#Escreva um algoritmo que leia três valores inteiros e mostre-os em ordem crescente#


n1 = int(input("Qual o primeiro número?"))
n2 = int(input("Qual o segundo número?"))
n3 = int(input("Qual o terceiro número?"))

if n1 <= n2 and n2 <= n3:
    print(n1, n2, n3)
else:
    if n1 <= n3 and n3 <= n2:
        print(n1, n3, n2)
    else:
        if n2 <= n1 and n1 <= n3:
            print(n2, n1, n3)
        else:
            if n2 <= n3 and n3 <= n1:
                print(n2, n3, n1)
            else:
                if n3 <= n1 and n1 <= n2:
                    print(n3, n1, n2)
                else:
                    if n3 <= n2 and n2 <= n1:
                        print(n3, n2, n1)
                        
            