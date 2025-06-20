# Aula 1 - Compreensão de lista (forma concisa de criar listas)

# Lista com quadrados de números de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

# Combinar duas listas com zip() e compreensão de lista
nomes = ["Alice", "Luan", "Paula"]
idades = [18, 25, 32]

# ERRO CORRIGIDO: estava usando variável errada (idades -> idade dentro da f-string)
combinacao = [f"{nome} tem {idade} anos" for nome, idade in zip(nomes, idades)]
print(combinacao)

# Lista com caracteres de uma string
letras = [letra for letra in "Python"]
print(letras)

# Dica: strings se comportam como listas em muitos aspectos (índice, len, for...)

# Aula 2 - Ordenação de listas

numeros = [1, 10, 5, 6, 8, 2, 7]
numeros.sort()  # Ordena a lista in-place (do menor para o maior)
print(numeros)

numeros.sort(reverse=True)  # Ordena do maior para o menor
print(numeros)

# Usando key para ordenar com base no comprimento das palavras
palavras = ["teste", "testando", "mais um teste"]
palavras.sort(key=len)  # Ordena do menor para o maior comprimento
palavras.sort(key=len, reverse=True)  # Agora do maior para o menor
print(palavras)

# sorted() retorna uma nova lista ordenada sem alterar a original
numeros_2 = sorted(numeros)
print(numeros)    # Original (ainda em ordem decrescente)
print(numeros_2)  # Nova lista ordenada crescente

# Aula 3 - Revertendo listas

cidades = ["São Paulo", "Rio De Janeiro", "Campo Grande"]

cidades.reverse()  # Inverte a lista in-place
print(cidades)

# reversed() retorna um iterador, por isso precisa ser convertido em lista
cidades_p = list(reversed(cidades))
print(cidades)   # A original continua invertida
print(cidades_p) # Essa é uma nova lista com reverso da original

# Outro exemplo
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

# Aula 4 - len, min, max, sum

numeros = [10, 20, 30, 40, 50]

print(len(numeros))  # Tamanho da lista

# Funções agregadoras
print("Valor máximo: ", max(numeros))
print("Valor mínimo: ", min(numeros))
print("Soma dos valores: ", sum(numeros))

# Usando key para comparar por tamanho de string
print("Maior cidade: ", max(cidades, key=len))
print("Menor cidade: ", min(cidades, key=len))
