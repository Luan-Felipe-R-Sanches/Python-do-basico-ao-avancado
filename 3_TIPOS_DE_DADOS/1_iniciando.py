# Aula 1 - Números Inteiros

numero1 = 41
numero2 = -12

print("Numeros: ", numero1, numero2)

# Mostra o tipo da variável (neste caso, int)
print(type(numero1))

# Função abs retorna o valor absoluto (positivo)
valor_absoluto = abs(numero2)
print(valor_absoluto)

# Função pow calcula potência (numero1 elevado a 2)
print(pow(numero1, 2))

# Soma entre dois inteiros
print(numero1 + numero2)


# Aula 2 - Operações Aritméticas

a = 20
b = 7

soma = a + b
multiplicacao = a * b
divisao = a // b  # Divisão inteira (descarta as casas decimais)
divisao_normal = a / b  # Divisão normal com ponto flutuante
subtracao = a - b

print("S: ", soma)
print("M: ", multiplicacao)
print("D sem resto, divisão inteira: ", divisao)
print("D normal: ", divisao_normal)
print("Sub: ", subtracao)

# Operador de módulo: retorna o resto da divisão
resto = a % b
print(resto)

# O contador não foi definido antes. Corrigido aqui:
contador = 0
contador += 10  # Incrementa 10 ao valor atual de contador
print(contador)


# Aula 3 - Float (Números de Ponto Flutuante)

temperatura = 32.1
pi = 3.14747574  # Corrigido o ponto decimal
altura = 1.80

print("Temperatura: ", temperatura)
print(type(temperatura))  # Mostra o tipo float

c = 1.8
d = 1.34458650

# Soma de dois floats
print(c + d)

# Notação científica: 1.5e6 = 1.500.000.0
numero_grande = 1.5e6
print(numero_grande)


# Aula 4 - Arredondamento e Módulo math

numero = 2.6575

# Arredonda o número para 2 casas decimais
num_arredondado = round(numero, 2)
print(num_arredondado)

import math
valor = 7.9

# math.ceil arredonda para cima
valor_cima = math.ceil(valor)

# math.floor arredonda para baixo
valor_baixo = math.floor(valor)

print(valor_cima, valor_baixo)
