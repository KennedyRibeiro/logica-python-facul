
n = 10

notas = [""] * n
i = 0 

while i < n:
    notas[i] = float(input("Nota: "))

    i += 1

media = 0
i = 0

while i < n:
    media += notas [i]

    i += 1

media = media / n
acima_media = 0
i = 0

while i < n:
    if notas[i] > media:
        acima_media += 1
    
    i += 1

print(media, acima_media)