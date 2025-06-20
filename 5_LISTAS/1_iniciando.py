# 1 - Listas

lista_vazia = []

print(lista_vazia)  # Lista vazia: []
print(len(lista_vazia))  # Tamanho da lista: 0

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1)
print(len(lista1))  # Tamanho da lista1: 3

# Concatenação de listas
lista_concatenada = lista1 + lista2
print(lista_concatenada)

# Repetição de elementos da lista
lista_repetida = lista1 * 3
print(lista_repetida)

# Verificação de existência de elementos
print(2 in lista1)
print(10 not in lista1)
print(5 not in lista2)

# Modificando elemento de uma lista pelo índice
lista1[0] = 10
print(lista1)

# Acessando elemento por índice (índices começam do 0)
print(lista1[2])

# Aula - adicionando elementos
animais = ["cachorro", "gato"]

animais.append("passaro")  # Adiciona no final
print(animais)

animais.insert(1, "coelho")  # Insere na posição 1
print(animais)

numeros = []
numeros.append(5)
numeros.insert(0, 10)  # Insere no início
print(numeros)


print(numeros)

# Aula 3 - remoção de itens
print(animais)

animais.remove("gato")  # Remove por valor
print(animais)

primeiro_el = animais.pop(0)  # Remove por índice e retorna o elemento
print(animais)
print(primeiro_el)

animais.pop()  # Remove o último elemento
print(animais)

# OBS: acessar índice ou remover elemento inexistente gera erro
