# Exercício 5:
# Enunciado: Escreva um programa que receba uma string, conte o número de vogais na string
# e exiba o total de vogais encontradas.
# Descrição: O programa deve iterar pela string, verificar se cada caractere é uma vogal e
# manter um contador que será exibido ao final.


texto = input("Digite uma string: ")

vogais = "aeiouAEIOU"  # Lista de vogais consideradas (maiúsculas e minúsculas)

# Gera 1 para cada caractere da string que é uma vogal e soma tudo
contador = sum(1 for char in texto if char in vogais)

print("Total de vogais: ", contador)
