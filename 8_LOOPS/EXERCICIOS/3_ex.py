# Exercício 3:
# Enunciado: Crie um programa que percorra uma lista de números e interrompa a iteração ao encontrar
# o primeiro número maior que 100. Use o comando `break` para encerrar o loop.
# Descrição: O programa deve iterar sobre a lista de números, verificar se cada número é maior que
# 100 e encerrar o loop ao encontrar a primeira ocorrência.

numeros = [10, 20, 30, 60, 120, 150]

for numero in numeros:
    if numero > 100:
        print(f"Primeiro numero encontrado acima de 100: {numero}")
        break  # Interrompe o loop ao encontrar o primeiro número > 100
    print(numero)  # Imprime os números até encontrar um acima de 100
