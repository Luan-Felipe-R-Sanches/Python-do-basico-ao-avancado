# Exercício 3:
# Enunciado: Desenvolva um programa que converta um número inteiro em float e vice-versa,
# exibindo o resultado das conversões.
# Descrição: O programa deve receber um número inteiro e convertê-lo em float, bem como receber
# um número float e convertê-lo em inteiro. Ambos os resultados das conversões devem ser exibidos.

numero_int = int(input("Digite um número inteiro: "))

numero_convertido_float = float(numero_int)

print(numero_convertido_float)

numero_float = float(input("Digite um número decimal: "))

numero_convertido_int = int(numero_float)

print(numero_convertido_float, numero_convertido_int)