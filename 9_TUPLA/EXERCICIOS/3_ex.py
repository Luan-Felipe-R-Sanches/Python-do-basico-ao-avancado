# Exercício 3:
# Enunciado: Converta a lista `[10, 20, 30, 40, 50]` em uma tupla. Em seguida, exiba o maior e o
# menor valor da tupla.
# Descrição: O programa deve usar a função `tuple()` para a conversão e as funções `max()` e `min()`
# para encontrar os valores máximo e mínimo.

lista = [10, 20, 30, 40, 50]

tupla = tuple(lista)  # Converte lista em tupla

# Usa funções embutidas para encontrar maior e menor valor da tupla
print(f"O maior valor é {max(tupla)} e o menor {min(tupla)}")
