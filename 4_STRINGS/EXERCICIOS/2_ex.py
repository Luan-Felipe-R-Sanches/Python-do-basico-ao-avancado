# Exercício 2:
# Enunciado: Escreva um programa que receba o nome completo de um usuário, divida o nome
# em partes e exiba o primeiro e o último nome separadamente.
# Descrição: O programa deve usar o método split() para dividir a string do nome em uma lista
# de palavras e acessar o primeiro e o último elementos da lista.

nome_completo = input("Digite o seu nome completo: ")

partes = nome_completo.split()  # Divide o nome em partes com base nos espaços

primeiro_nome = partes[0]       # Primeiro nome sempre é o primeiro item

# CUIDADO: Isso pode causar erro se a pessoa digitar só um nome
# ultimo_nome = partes[1]

# Solução mais segura:
ultimo_nome = partes[-1]        # Pega o último nome, independente do número de partes

print("Primeiro nome: ", primeiro_nome)
print("Último nome: ", ultimo_nome)
