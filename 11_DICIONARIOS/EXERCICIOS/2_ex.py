# EXERCÍCIO 2: Acessando e filtrando valores em um dicionário
# ESCRIÇÃO: Dado um dicionário com produtos e seus preços, filtre apenas os produtos com preço
# acima de R$50,00. Exiba o nome e o preço de cada produto que atenda a esse critério.

produtos = {
    "Computador": 3000.50,
    "Liquidificador": 80.44,
    "Mouse": 44.12,
    "Teclado": 122.10,
}

produtos_filtrados = {
    produto: preco for produto, preco in produtos.items() if preco > 50.0
}

print(produtos_filtrados)
