#função, procedimento, modularização

nota1 = int(input("Nota 1 :"))
nota2 = int(input("Nota 2 :"))
media = (nota1 + nota2) / 2

print(media)

if media >= 70:
    print("Aprovado")
elif media >= 30:
    print("Exame")
else:
    print("Reprovado")