# Exercício 4:
# Enunciado: Crie um programa que solicite três números ao usuário, aplique a fórmula de
# Bhaskara para calcular as raízes e exiba os resultados.
# Descrição: O programa deve solicitar os coeficientes `a`, `b` e `c` da equação quadrática.
# Usar o módulo math para calcular a raiz quadrada na fórmula de Bhaskara e exibir as raízes,
# se existirem. Deve incluir validação para o caso de raízes inexistentes.

import math


a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

print(raiz1, raiz2)