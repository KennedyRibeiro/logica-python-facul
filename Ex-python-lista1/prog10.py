#Desenvolva um algoritmo para calcular o peso ideal de uma pessoa, utilizando as seguintes fórmulas: Peso ideal para homens = (72,7 H) – 58, Peso ideal para mulheres = (62,1 H) – 44,7, onde H = altura. O algoritmo deverá mostrar ambos os resultados, não se importando com o sexo da pessoa. O valor H deverá ser lido.#


altura = float(input("qual é a altura?"))
peso_home = (72.7 * altura) - 58
peso_mulh = (62.1 * altura) - 44.7
print("O peso ideal masculino: ",peso_home, "O peso ideal feminino", peso_mulh)
