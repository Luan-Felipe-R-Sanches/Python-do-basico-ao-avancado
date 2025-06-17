# Exercício 5:
# Enunciado: Escreva um programa que use o módulo `math` para calcular a área de um círculo,
# solicitando o raio ao usuário.
# Descrição: O programa deve solicitar o raio como entrada, usar a fórmula da área de um
# círculo (A = πr²), com o módulo math para calcular π, e exibir o resultado com duas casas
# decimais.

raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio**2)

print(area)