# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.
# Descrição: O programa deve utilizar a função print() para exibir a mensagem
# "Olá, Mundo!" no console. Este exercício reforça o uso básico da função
# print() e a estrutura simples de um programa Python.

# Exercício 2:
# Enunciado: Escreva um programa que solicite o nome do usuário e exiba uma
# saudação personalizada.
# Descrição: O programa deve usar a função input() para receber o nome do
# usuário e armazená-lo em uma variável. Em seguida, deve exibir uma mensagem
# de saudação que inclua o nome fornecido, utilizando a função print().

# Exercício 3:
# Enunciado: Desenvolva um programa que demonstra o uso correto da indentação
# em uma estrutura condicional.
# Descrição: O programa deve solicitar um número ao usuário e verificar se ele
# é positivo, negativo ou zero. Utilize estruturas condicionais com a
# indentação adequada para determinar e exibir o resultado.

# Exercício 4:
# Enunciado: Crie um programa que solicita dois números ao usuário e exibe a
# soma deles.
# Descrição: O programa deve utilizar a função input() para receber dois
# números, converter as entradas para o tipo numérico apropriado float(), calcular a
# soma e exibir o resultado utilizando print().

# Exercício 5:
# Enunciado: Escreva um programa que calcula a idade do usuário com base no ano
# de nascimento fornecido.
# Descrição: O programa deve solicitar o ano de nascimento do usuário, converter
# a entrada para inteiro, calcular a idade atual considerando o ano atual e
# exibir a idade utilizando print(). Utilize comentários para explicar cada
# etapa do código.

# EX1
#print("Olá, Mundo!")

# EX2
#nome_usuario = input()
#print(nome_usuario, "Bem-vindo ao Python!")

# EX3
# Solicita um número ao usuário
# numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
# if numero > 0:
#    print("O número é positivo.")
# elif numero < 0:
#    print("O número é negativo.")
# else:
#    print("O número é zero.")

#EX4
#n1 = float(input("Digite o primeiro número: "))
#n2 = float(input("Digite o segundo número: "))

#soma = n1 + n2;
#print("A soma dos números é ", soma)

#EX5
from datetime import datetime  # Importa o módulo para obter o ano atual

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Qual o ano do seu nascimento? "))

# Calcula a idade com base no ano atual
idade = datetime.now().year - ano_nascimento

# Exibe a idade do usuário
print("Sua idade é:", idade)
