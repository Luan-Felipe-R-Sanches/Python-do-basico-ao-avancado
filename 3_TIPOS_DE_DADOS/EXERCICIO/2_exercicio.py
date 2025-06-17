# Exercício 2:
# Enunciado: Escreva um programa que receba um número de ponto flutuante, arredonde-o para duas
# casas decimais e exiba o resultado.
# Descrição: O programa deve solicitar um número float, usar a função round() para arredondá-lo
# para duas casas decimais e exibir o valor arredondado. O programa também deve informar o número
# original.

num = float(input("Digite um número decimal: "))
decimal = round(num)

print("Número original: ", num)
print("Número Arredondado: ", decimal)