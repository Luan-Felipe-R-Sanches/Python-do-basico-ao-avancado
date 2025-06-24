# Exercício 2:
# Enunciado: Desenvolva um programa que itere sobre uma string fornecida pelo usuário e conte
# quantas vogais estão presentes nela. Use um loop `for` e o comando `continue` para ignorar
# caracteres que não são vogais.
# Descrição: O programa deve iterar sobre a string, verificar se cada caractere é uma vogal e
# atualizar um contador para as vogais encontradas.

string = input("Digite alguma coisa... ")

vogais = "aeiouAEIOU"  # Lista de vogais consideradas (maiúsculas e minúsculas)

contador = 0  # Contador de vogais

for char in string:
    if char not in vogais:
        continue  # Ignora caracteres que não são vogais
    contador += 1  # Incrementa se for vogal

print(f"A quantidade de vogais na string é: {contador}")
