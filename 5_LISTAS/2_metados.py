# Aula 1 - Métodos úteis
frutas = ["maça", "banana", "Laranja", "Melancia", "morango", "banana"]

print(frutas.count("banana"))  # Conta quantas vezes "banana" aparece
print(frutas.count("maça"))
print(frutas.count("Kiwi"))  # Elemento inexistente: retorna 0

print(frutas.index("banana"))  # Retorna o índice da primeira ocorrência
print(frutas.index("Melancia"))

# OBS: procurar o índice de um item inexistente causa erro

# Limpa todos os elementos da lista
teste = frutas.clear()

print(teste)  # None (clear não retorna nada)
print(frutas)  # Lista vazia: []

# Aula 2 - Listas aninhadas (listas dentro de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz)
print(matriz[0])  # A primeira sublista


print(matriz[1][2])  # Acessa linha 1, coluna 2 -> valor 6

# Adiciona nova linha à matriz
nova_linha = [10, 11, 12]
matriz.append(nova_linha)
print(matriz)

# Aula 3 - Continuando listas aninhadas

print(matriz[2][0])  # Linha 3, coluna 1 -> valor 7

matriz[0][1] = 99  # Altera valor na posição [0][1]
print(matriz)

matriz.pop(1)  # Remove a linha de índice 1 (segunda linha)
print(matriz)

matriz[0].append(123)  # Adiciona valor à sublista na primeira linha
print(matriz)

# Podemos aplicar métodos de lista em sublistas também
matriz.append([4, 4, 4])  # Adiciona nova sublista
print(matriz)

# Aula 4 - Iterando sobre listas
lista_nova = [1, 2, 3, 4, 5]

# Loop simples sobre a lista
for numero in lista_nova:
    print("O número da vez é", numero)

# Loop com índice e valor usando enumerate()
for i, linha in enumerate(matriz):
    print(f"Linha {i + 1}: {linha}")

# Iterando sobre cada número de cada linha da matriz
for linha in matriz:
    print(linha)
    for numero in linha:
        print("valor:", numero)

# Loop while como alternativa ao for
i = 0
while i < len(lista_nova):
    print("Número:", lista_nova[i])
    i += 1
