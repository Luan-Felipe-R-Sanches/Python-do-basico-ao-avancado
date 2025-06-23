# Aula 1 - Operadores de identidade
x = None

# 'is' verifica se duas variáveis apontam para o mesmo objeto na memória
print(x is None)       # True
print(x == None)       # True, mas o recomendado é usar 'is None'
print(x is not None)   # False

a = 10
b = 10

# Cuidado: para números pequenos (inteiros até 256), Python reutiliza o mesmo objeto
print(a is b)          # True (inteiros pequenos são "internados")
print(a == b)          # True

lista = [1, 2, 3]
lista2 = [1, 2, 3]

print(lista is lista2)  # False, pois são dois objetos diferentes em memória
print(lista == lista2)  # True, pois o conteúdo é igual

s1 = "Python"
s2 = "Python"

# Strings literais iguais geralmente são internadas (apontam pro mesmo lugar)
print(s1 is s2)        # True (por otimização do Python)
print(s1 == s2)        # True

d = {}
d2 = {}

print(d is d2)         # False, são dicionários distintos
print(d == d2)         # True, ambos estão vazios

t = ()
t2 = ()

print(t is t2)         # True, tuplas vazias são internadas (otimizadas)

# Aula 2 - Operadores de associação
frutas = ["Maçã", "Banana", "Laranja"]

# 'in' verifica se um elemento está presente
print("Maçã" in frutas)       # True
print("Abacate" not in frutas)  # True

frase = "Python é muito legal"

print("Python" in frase)      # True
print("Java" in frase)        # False

# Tupla = lista imutável
numeros = (1, 2, 3, 4, 5)

print(1 in numeros)           # True
print(10 in numeros)          # False

# Dicionários = estrutura de dados com chave:valor
pessoa = {"nome": "Matheus", "idade": 33}

# Verifica se uma chave existe
print("profissao" in pessoa)       # False

# Verifica se um valor existe
print("Joaquim" in pessoa.values())  # False

# Aula 3 - Operadores com condições e cálculos

# input() sempre retorna uma string, por isso precisa de conversão
entrada = input("Digite um número: ")

numeros = [1, 2, 3, 4, 5]

# Verifica se o número digitado está na lista
if int(entrada) in numeros:
    print("Você acertou!")

idade = 25
renda = 6000

# Ambas as condições precisam ser verdadeiras
if idade < 30 and renda > 5000:
    print("Você ganha bem!")

frase = "PHP e Python são linguagens de programação"

# Ambas palavras precisam estar presentes
if "Python" in frase and "PHP" in frase:
    print("O texto fala sobre Python e PHP")
