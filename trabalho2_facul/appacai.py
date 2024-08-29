from calcularAcai import calcular_valor

print("--------------------------------------------------")
print("  Bem-Vindo a sorveteria e Lanchonete do Kennedy  ")
print("--------------------Cardápio----------------------")
print("------| Tamanho | Cupuaçu (CP) | Açaí (AC) |------")
print("------|    P    |   R$ 10,00   | R$ 12,00  |------")
print("------|    M    |   R$ 15,00   | R$ 17,00  |------")
print("------|    G    |   R$ 19,00   | R$ 21,00  |------")
print("--------------------------------------------------")

valor_total = 0

while True:
    sabor = input("Escolha o sabor desejado (CP|AC): ").upper()
    
    if sabor not in ["CP", "AC"]:
        print("Sabor inválido. Tente novamente.")
        continue

    tamanho = input("Escolha o tamanho desejado (P|M|G): ").upper()

    if tamanho not in ["P", "M", "G"]:
        print("tamanho inválido. Tente novamente.")
        continue

    valor_pedido = calcular_valor(sabor, tamanho)
    valor_total += valor_pedido
    print(f"Você pediu {sabor} {tamanho}, o pedido fica em: R$ {valor_pedido:.2f}")

    mais = input("Deseja mais alguma coisa? (sim ou não) ").lower()
    if mais != "sim":
        break

print(f"O valor total a ser pago: R$ {valor_total:.2f}")