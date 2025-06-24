# Exercício 5:
# Enunciado: Implemente um programa que filtre números pares de uma lista e categorize os números
# pares como "pequenos" (menores que 10) ou "grandes" (10 ou maiores). Use condicionais e boas
# práticas de codificação.
# Descrição: O programa deve iterar pela lista, usar condicionais para categorizar os números pares,
# e exibir as categorias.

numeros = [3, 12, 7, 5, 8, 11, 90, 4]

pares = [num for num in numeros if num % 2 == 0]

print(pares)

categorias = [
    "Pequeno" if num < 10 else "Grande" for num in pares
]

print(categorias)