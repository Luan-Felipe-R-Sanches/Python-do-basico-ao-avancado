# 1 - frozenset
lista = [1, 2, 3, 4, 5]

# frozenset cria um conjunto imutável (não pode ser modificado)
fs = frozenset(lista)
print(fs)

fs2 = frozenset([4, 5, 6, 7])

# Operações de conjunto como union e intersection funcionam com frozenset
print(fs.union(fs2))
print(fs.intersection(fs2))

# fs.add(x) -> erro, pois frozenset é imutável
# fs.remove(2) -> erro pelo mesmo motivo

# frozenset pode ser usado como chave de dicionário (diferente de set, que é mutável)
dicionario = {fs: "Teste"}
print(dicionario)

# 2 - diferenças entre tipos de coleções e operações

lista = [1, 2, 3, 4, 4]

# Conversão de lista para conjunto remove duplicatas
conj = set(lista)
print(conj)

# Interseção entre duas listas (convertidas para set)
lista2 = [2, 3, 6, 7]
print(list(set(lista) & set(lista2)))  # Resultado convertido de volta para lista

# Tupla convertida em conjunto
tupla = (1, 2, 3)
conj3 = set(tupla)
print(conj3)
