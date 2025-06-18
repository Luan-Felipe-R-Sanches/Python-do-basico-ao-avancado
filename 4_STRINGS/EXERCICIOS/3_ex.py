# Exercício 3:
# Enunciado: Desenvolva um programa que solicite uma lista de itens separados por vírgulas
# e os exiba em uma única string, com os itens separados por ponto e vírgula.
# Descrição: O programa deve receber uma entrada de texto, usar o método split() para criar
# uma lista e depois o método join() para concatenar os itens com o delimitador ";".

itens = input("Digite uma lista de itens separados por vírgula: ")

lista = itens.split(",")  # Divide os itens com base na vírgula

# OPÇÃO MELHORADA: remove espaços em branco extras de cada item
lista = [item.strip() for item in lista]

resultado = ";".join(lista)  # Junta os itens com ponto e vírgula como separador

print("Itens formatados: ", resultado)
