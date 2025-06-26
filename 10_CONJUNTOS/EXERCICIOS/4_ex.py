# Exercício 4:
# Enunciado: Crie um programa que itere sobre dois conjuntos e encontre a diferença simétrica 
# entre eles. Imprima os elementos exclusivos de cada conjunto.
# Descrição: O programa deve calcular a diferença simétrica entre dois conjuntos usando o operador 
# `^` e exibir os resultados.

conj_a = {1, 2, 3, 4}
conj_b = {4, 5, 6, 7}

# Diferença simétrica: elementos que estão em apenas um dos conjuntos
diferenca = conj_a ^ conj_b  # O operador ^ retorna elementos exclusivos de cada conjunto

print(diferenca)
