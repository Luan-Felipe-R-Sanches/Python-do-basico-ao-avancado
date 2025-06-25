# Exercício 4:
# Enunciado: Crie um programa que itere sobre uma tupla de números e calcule a soma apenas dos
# números pares presentes nela.
# Descrição: O programa deve iterar sobre a tupla, verificar se cada número é par e somar os pares.

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

soma_pares = 0

# Itera sobre a tupla e acumula a soma dos números pares
for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma foi: {soma_pares}")
