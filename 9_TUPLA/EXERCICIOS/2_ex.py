# Exercício 2:
# Enunciado: Defina uma função que receba dois números como parâmetros e retorne uma tupla contendo
# a soma, a diferença e o produto dos números. Mostre como acessar cada valor retornado separadamente.
# Descrição: A função deve calcular e retornar os valores como uma tupla. O programa deve usar
# desempacotamento para acessar os valores.


def operacoes(n1, n2):
    # Retorna soma, subtração e multiplicação como uma tupla
    return n1 + n2, n1 - n2, n1 * n2

resultado = operacoes(10, 5)

# Acessa os resultados pela tupla retornada usando índices
print(f"Soma: {resultado[0]}, Subtração: {resultado[1]}, Multiplicação: {resultado[2]}")
