precoCompras = float(input("Preço das compras? R$"))

print("""
FORMAS DE PAGAMENTO
[ 1 ] à vista em dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")

opcao = int(input("Qual é a opção? "))
desconto = 0
valorFinal = 0

if opcao == 1:
    desconto = precoCompras * 0.1
    valorFinal = precoCompras - desconto
    print(f"Sua compra de R${precoCompras:.2f} vai custar R${valorFinal:.2f}")
elif opcao == 2:
    desconto = precoCompras * 0.05
    valorFinal = precoCompras - desconto
    print(f"Sua compra de R${precoCompras:.2f} vai custar R${valorFinal:.2f}")
elif opcao == 3:
    valorFinal = precoCompras
    valorParcelado = valorFinal / 2
    print(f"Sua compra será parcelada em {2}x de R${valorParcelado:.2f} ")
    print(f"Sua compra de R${precoCompras:.2f} vai custar R${valorFinal:.2f}")

elif opcao == 4:
    juros = precoCompras * 0.2
    parcelas = int(input("Quantas parcelas? "))
    valorFinal = precoCompras + juros
    valorParcelado = valorFinal / parcelas

    print(f"Sua compra será parcelada em {parcelas}x de R${valorParcelado:.2f} com juros ")
    print(f"Sua compra de R${precoCompras:.2f} vai custar R${valorFinal:.2f}")
else:
    print("Você selecionou uma opção invalida")