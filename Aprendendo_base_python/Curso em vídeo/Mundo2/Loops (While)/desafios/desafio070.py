print("-"*20)
print("Loja SUPER BARATÂO")
print("-"*20)
totalConta = totalProdutos = totalProdutoMaisDeMil = precoPodutoMaisBarto = 0
nomeProdutoMaisBarato = ""
while True:
    nomeProduto = input("Nome do produto: ").strip()
    preco = float(input("Preço produto: R$"))
    totalConta += preco
    totalProdutos += 1
    if preco > 1000: totalProdutoMaisDeMil+=1

    if precoPodutoMaisBarto > preco or totalProdutos == 1:
        nomeProdutoMaisBarato = nomeProduto
        precoPodutoMaisBarto = preco


    opcao = input("Quer continuar? [S/N] ").strip().lower()
    if opcao == "n": break

print("-"*10, "FIM DO PROGRAMA", "-"*10)
print(f"O total da compra foi R${totalConta:.2f}")
print(f"Temos {totalProdutoMaisDeMil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {nomeProdutoMaisBarato} que custa R${precoPodutoMaisBarto}")