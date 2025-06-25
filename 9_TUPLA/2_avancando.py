# 1 - Tuplas em funções

def dividir(numerador, denominador):
    quociente = numerador // denominador
    resto = numerador % denominador
    return quociente, resto  # Retorna uma tupla com quociente e resto

resultado = dividir(10, 3)
print(resultado)

print(f"Quociente {resultado[0]} e Resto {resultado[1]}")  # Acesso por índice

quociente, resto = dividir(20, 2)  # Desempacotamento direto da tupla retornada
print(quociente, resto)

def calcular_area(dimensoes):
    largura, altura = dimensoes  # Desempacotamento de tupla passada como argumento
    return largura * altura

area = calcular_area((5, 4))  # Tupla como argumento
print(area)

# 2 - Conversões entre listas e tuplas
lista = [4, 5, 6]

tupla = tuple(lista)  # Converte lista para tupla
print(tupla)

lista_da_tupla = list(tupla)  # Converte tupla para lista
print(lista_da_tupla)

# Strings para lista ou tupla

texto = "PYTHON"

tupla_text = tuple(texto)  # Cada caractere vira um elemento da tupla
lista_texto = list(texto)  # Cada caractere vira um elemento da lista

print(tupla_text)
print(lista_texto)

# tuple e list não modificam o dado original, apenas retornam uma nova estrutura

# 3 - Diferença entre listas e tuplas

l = [1, 2, 3]
t = (1, 2, 3)

# t[0] = 1  # ERRO: tuplas são imutáveis

l[0] = 2  # Listas são mutáveis

import timeit

# Medindo o tempo de criação de listas e tuplas
tempo_lista = timeit.timeit("[1, 2, 3, 4, 5]", number=1000000)
tempo_tupla = timeit.timeit("(1, 2, 3, 4, 5)", number=1000000)

print(f"Tempo lista: {tempo_lista} e Tempo tupla: {tempo_tupla}")
