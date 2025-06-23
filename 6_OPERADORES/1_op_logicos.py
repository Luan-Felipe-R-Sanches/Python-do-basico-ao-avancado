# Aula 1 - Operadores de comparação
a = 5
b = 10

# Comparação de igualdade
print(a == b)  # False, pois 5 não é igual a 10
print(a != b)  # True, pois 5 é diferente de 10

# >  -> maior que
# <  -> menor que
print(a > b)   # False
print(b > a)   # True
print(a < b)   # True

c = 10
d = 11

# >= -> maior ou igual
# <= -> menor ou igual
print(b >= c)  # True, pois 10 é igual a 10
print(b > c)   # False, pois 10 não é maior que 10

# >= ou <= também validam igualdade entre os valores
print(a <= d)  # True, pois 5 é menor que 11

# Aula 2 - Continuando operadores
x = 10
y = 25

print(x != y)  # True

z = 20

# Avaliação encadeada: (x < y) and (y < z)
print(x < y < z)  # True, pois 10 < 25 e 25 < 20 => False

# Comparação entre tipos de dados diferentes
valor = "5"
x = 5

print(valor == x)          # False, pois "5" (str) não é igual a 5 (int)
print(int(valor) == x)     # True, convertendo "5" para inteiro

# Gera um erro se tentar comparar string com inteiro usando '>'
# print(valor > x)  # TypeError

# Aula 3 - Operadores lógicos
idade = 17

# and -> todas as condições devem ser verdadeiras
print(idade > 18 and idade < 30)  # False, pois 17 não é maior que 18

# or -> pelo menos uma das condições deve ser verdadeira
print(idade < 18 or idade > 65)   # True, pois 17 é menor que 18

# not -> inverte o valor booleano
print(not True)  # False

# Exemplo com not em uma variável
# idosa = False
# print(not idosa)  # True

a = 10
b = 5
c = 6
d = 7

# or -> uma das condições deve ser verdadeira
print(a > b or c == d)  # True, pois a > b é True

# not tem precedência: not (a > b) é False -> False or False = False
print((not a > b or c == d))  # False
