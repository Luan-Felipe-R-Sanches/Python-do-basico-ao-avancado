# Exercício 5:
# Enunciado: Converta uma lista de nomes com duplicatas em um conjunto para remover os duplicados. 
# Em seguida, adicione um novo nome ao conjunto e imprima o resultado.
# Descrição: O programa deve converter uma lista em um conjunto, remover duplicatas automaticamente, 
# adicionar um novo nome e exibir o resultado.
nomes = ["Ana", "João", "Ana", "João", "Pedro"]

# Conversão de lista para conjunto elimina duplicatas automaticamente
conj_nomes = set(nomes)  # Resultado: {'Ana', 'João', 'Pedro'}

# Adição de novo nome ao conjunto
conj_nomes.add("Carlos")  # Adiciona apenas se ainda não estiver presente

print(conj_nomes)
