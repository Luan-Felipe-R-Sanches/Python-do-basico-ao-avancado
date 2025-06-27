# EXERCÍCIO 4: Compreensão de dicionários com listas de números
# DESCRIÇÃO: Usando uma lista de números, crie um dicionário onde a chave é o número e o valor 
# é o quadrado do número. Exiba o dicionário completo ao final.

numeros = [1, 2, 3, 4, 5]

quadrados = {num: num ** 2 for num in numeros}

print(quadrados)