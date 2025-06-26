# Exercício 3:
# Enunciado: Utilize `frozenset` para criar um conjunto imutável com os números de 1 a 5. 
# Tente adicionar um elemento ao conjunto e exiba a mensagem de erro gerada.
# Descrição: O programa deve criar um `frozenset`, tentar adicionar um elemento e capturar 
# o erro gerado.

# Criação de um conjunto imutável com frozenset
conj_imutavel = frozenset([1, 2, 3])  # frozenset é como set, mas não permite alterações

try:
    conj_imutavel.add(5)  # Tentativa de modificação gera erro, pois frozenset é imutável
except AttributeError:
    print("Ocorreu um erro")  # Captura o erro ao tentar modificar o frozenset
