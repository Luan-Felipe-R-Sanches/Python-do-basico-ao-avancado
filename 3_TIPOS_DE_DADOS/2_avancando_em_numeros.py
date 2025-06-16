# Aula 1 - Números Complexos

numero1 = 3 + 4j
numero2 = 2 - 1j

print(numero1)  # Exibe o número complexo
print(numero2)

# Criação de número complexo usando a função complex(real, imag)
numero3 = complex(5, -3)
print(numero3)

# Atributos dos números complexos
print(numero1.real)  # Parte real
print(numero2.imag)  # Parte imaginária


# Aula 2 - Conversões de Tipos Numéricos

numero_int = 10

# Conversão de inteiro para float
numero_float = float(numero_int)
print(numero_float)

# Conversão de float para complexo
numero_complex = complex(numero_float)
print(numero_complex)

# Operações com tipos mistos (int + float)
print(10 + 10.4)  # Resultado é float

# Conversão de float para inteiro (trunca a parte decimal)
print(int(10.44))


# Aula 3 - Operações Aritméticas

a = 10
b = 3

# Operações básicas
print(a + b)  # Soma
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão normal (float)
print(a // b) # Divisão inteira (descarta parte decimal)
print(a % b)  # Módulo (resto da divisão)
print(a ** b) # Potência


# Aula 4 - Precedência de Operadores

resultado = 3 + 4 * 5
print(resultado)  # Multiplicação tem prioridade: 3 + (4 * 5) = 23

resultado2 = (3 + 4) * 5
print(resultado2)  # Parênteses alteram a ordem: (3 + 4) * 5 = 35

exp = 2 ** 3 ** 2
print(exp)  # Exponenciação é avaliada da direita para a esquerda: 2 ** (3 ** 2) = 512

op_complexas = (10 + 5) * 2 - (33 + 4 / 2)
print(op_complexas)  # Respeita ordem de operações e parênteses


# Aula 5 - Funções Matemáticas

numero = -15
numero_abs = abs(numero)  # Retorna valor absoluto
print(numero_abs)

numero_quebrado = 1.42354567
print(round(numero_quebrado, 2))  # Arredonda para 2 casas decimais

base = 2
expoente = 5
modulo = 3

# pow(x, y, z) calcula (x ** y) % z de forma eficiente
resultado = pow(base, expoente, modulo)
print(resultado)

# divmod(x, y) retorna uma tupla com (quociente, resto)
quociente, resto = divmod(20, 6)
print(quociente, resto)
