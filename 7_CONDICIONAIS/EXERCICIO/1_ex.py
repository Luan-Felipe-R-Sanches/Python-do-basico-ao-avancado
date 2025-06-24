# Exercício 1:
# Enunciado: Escreva um programa que receba a idade de uma pessoa e exiba uma mensagem indicando se
# ela é criança (menor de 13 anos), adolescente (13 a 17 anos) ou adulta (18 anos ou mais) usando
# estruturas if-elif-else.
# Descrição: O programa deve capturar a idade, usar condicionais para determinar a faixa etária e
# exibir a mensagem correspondente.

idade = 6

if idade < 13:
    print("Você é uma criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")

