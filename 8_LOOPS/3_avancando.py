# Aula 1 - Loops aninhados

matriz = [[1, 2, 3], [4, 5, 6], [9, 8, 7]]

for linha in matriz:
    print(linha)  # Imprime a linha completa
    for elemento in linha:
        print(f"Elemento: {elemento}")  # Itera por cada elemento da linha
lista1 = [1, 2, 3]
lista2 = [2, 5, 7]

for a in lista1:
    for b in lista2:
        if a == b:
            print("Iguais")  # Imprime se os elementos são iguais
        print(f"Comparando {a} e {b}")  # Mostra todas as comparações
