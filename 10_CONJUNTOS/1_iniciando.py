# 1 - criando conjuntos - set
conjunto = {1, 2, 3, 4}
print(conjunto)

# Conversão de lista com elementos repetidos para conjunto remove duplicatas
conjunto_de_lista = set([1, 2, 3, 3])
print(conjunto_de_lista)

print(len(conjunto_de_lista))  # Conta apenas elementos únicos

# Verificação de existência (rápida em conjuntos)
print(4 in conjunto_de_lista)
print(1 in conjunto_de_lista)

# 2 - operações matemáticas entre conjuntos
conj1 = {1, 2, 3}
conj2 = {2, 3, 4, 5}

uniao = conj1 | conj2  # União: todos os elementos, sem duplicatas
print(uniao)

interseccao = conj1 & conj2  # Interseção: apenas os elementos em comum
print(interseccao)

diferenca = conj1 - conj2  # Diferença: elementos exclusivos de conj1
print(diferenca)

diferenca2 = conj2 - conj1  # Diferença: elementos exclusivos de conj2
print(diferenca2)

# Os mesmos resultados, agora com métodos explícitos (mais legível em alguns casos)
print(conj1.union(conj2))
print(conj1.intersection(conj2))
print(conj1.difference(conj2))
print(conj2.difference(conj1))

# 3 - operações avançadas

# Diferença simétrica: elementos exclusivos de cada conjunto
sim = conj1 ^ conj2
print(sim)

sim2 = conj1.symmetric_difference(conj2)
print(sim2)

subconjunto = {1, 2}
subconj2 = {99, 101}

# Verifica se todos os elementos de subconjunto estão em conj1
print(subconjunto.issubset(conj1))  # True
print(subconj2.issubset(conj1))     # False

# 4 - métodos de conjunto
conj3 = {1, 2, 3, 4, 5, 6, 7, 8}

conj3.add(5)   # Já existe, nada muda
conj3.add(10)  # Novo elemento, será adicionado
print(conj3)

conj3.remove(3)     # Remove um elemento existente
conj3.discard(99)   # Tenta remover, mas não gera erro se não existir
# conj3.remove(99)  # Geraria erro se descomentado

print(conj3)

conj3.clear()  # Esvazia completamente o conjunto
print(conj3)
