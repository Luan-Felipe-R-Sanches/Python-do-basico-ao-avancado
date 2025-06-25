# 1 - Criando tuplas
tupla = (1, 2, 3)
print(tupla)

tupla_lista = tuple([1, 2, 3])  # Conversão de lista para tupla
print(tupla_lista)

tupla_1_el = (1,)  # Tupla com um único elemento (vírgula é obrigatória)
print(tupla_1_el)

tupla_vazia = ()
print(tupla_vazia)

# Aula 2 - Imutabilidade
tupla = (1, 2, 3, 4)

# tupla[0]=10  # ERRO: tuplas são imutáveis, não é possível alterar elementos

print(tupla[0])  # Acesso por índice

tupla_nova = tupla + (5, 6, 7)  # Gera nova tupla com concatenação
print(tupla_nova)

ocorrencias = tupla.count(3)  # Conta quantas vezes o valor 3 aparece
print(ocorrencias)

print(tupla_nova.index(7))  # Retorna índice do valor 7

# 3 - Operações com tuplas
print(tupla_nova[3])  # Acesso por índice

subtupla = tupla_nova[2:5]  # Fatiamento da tupla
print(subtupla)

tupla = (10, 20)

tupla_maior = tupla_nova + tupla  # Concatenação de tuplas
print(tupla_maior)

tupla_repetida = tupla_nova * 3  # Repetição da tupla
print(tupla_repetida)

# 4 - Desempacotamento
tuplas_teste = ("a", "b", "c")
um, dois, tres = tuplas_teste  # Atribuição múltipla por desempacotamento
print(um, dois, tres)

a, *extras = tupla_repetida  # Desempacota o primeiro elemento e agrupa o resto em uma lista
print(a)
print(extras)

tuplas = [(1, 14), (22, 12), (44, 45)]
for x, y in tuplas:  # Desempacotamento dentro do loop
    print("Coordenadas x e y: ", x, y)
