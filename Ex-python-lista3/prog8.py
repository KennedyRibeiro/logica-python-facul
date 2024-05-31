# A série de Fibonacci é formada pela seguinte sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... etc. Escreva um algoritmo que gere a série de Fibonacci até o vigésimo termo.

n = 0

anterior = 1
proximo = 1
atual = 0

while atual <= 21:
    proximo = atual + anterior
    anterior = atual
    atual = proximo

    print(atual)