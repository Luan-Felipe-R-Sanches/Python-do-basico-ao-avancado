# Exercício 4:
# Enunciado: Escreva um programa que utilize loops aninhados para criar uma tabela de multiplicação
# de 1 a 5. Formate a saída em forma de matriz para facilitar a leitura.
# Descrição: O programa deve usar loops `for` aninhados para calcular e exibir os resultados da
# multiplicação em formato tabular.

for i in range(1, 6):          # Linha da tabuada (1 a 5)
    for j in range(1, 6):      # Coluna da tabuada (1 a 5)
        print(f"{i * j}", end=" ")  # Imprime o produto na mesma linha
    print()  # Quebra de linha após cada linha da tabuada
