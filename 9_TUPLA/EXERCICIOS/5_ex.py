# Exercício 5:
# Enunciado: Escreva um programa que compare o desempenho de listas e tuplas na iteração de
# 1 milhão de elementos, exibindo o tempo de execução de cada uma.
# Descrição: O programa deve usar a biblioteca `timeit` para medir o tempo de execução de um loop
# iterando sobre uma lista e uma tupla.

lista = list(range(1_000_000))
tupla = tuple(range(1_000_000))

import timeit

# Mede o tempo para iterar 1000 vezes sobre a lista
tempo_lista = timeit.timeit(
    stmt="for x in lista: pass", setup="lista = list(range(1_000_000))", number=1000
)

# Mede o tempo para iterar 1000 vezes sobre a tupla
tempo_tupla = timeit.timeit(
    stmt="for x in tupla: pass", setup="tupla = tuple(range(1_000_000))", number=1000
)

print(f"Tempo de execução lista {tempo_lista:.5f} segundos")
print(f"Tempo de execução tupla {tempo_tupla:.5f} segundos")
