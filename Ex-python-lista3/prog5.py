# Prepare um algoritmo que calcule o valor de H, sendo que ele é determinado pela série H = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.


h = 0
num = 1
den = 1

while den <= 50:
    h = num / den
    num = num + 2
    den = den + 1

print("O valor de H é: ", h)
