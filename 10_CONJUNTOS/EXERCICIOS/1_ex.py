# Exercício 1:
# Enunciado: Crie um conjunto que armazene os números de 1 a 5. Em seguida, verifique se o número 3 
# está presente no conjunto e imprima o resultado.
# Descrição: O programa deve criar um conjunto com os números de 1 a 5, verificar a presença do número 
# 3 usando o operador `in` e exibir o resultado.

# Criação de um conjunto com os números de 1 a 5
numeros = {1, 2, 3, 4, 5}  # Conjuntos não permitem elementos repetidos e têm busca rápida por valor

# Verificação da presença do número 3 no conjunto
print(f"O numero 3 está no conjunto? {'Sim' if 3 in numeros else 'Não'}")  # Uso do operador 'in' é eficiente em conjuntos
