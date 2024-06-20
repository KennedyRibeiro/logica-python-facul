def media_arit(nota1, nota2):
    media_final = (nota1 + nota2) / 2
    return media_final


def situacao_aluno(media_aluno):
    if media_aluno >= 70:
        print('Aluno APROVADO com média =', media_aluno)
    else:
        if media_aluno >= 30:
            print('Aluno EM EXAME com média =', media_aluno)
        else:
            print('Aluno REPROVADO com média =', media_aluno)


def main():
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    media = media_arit(nota1, nota2)
    situacao_aluno(media)


main()
