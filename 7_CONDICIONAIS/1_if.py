# Aula 1 - if
if True:
    print("Deu certo")        # Será executado, pois a condição é True
    print("Outra linha")      # Também será executada

numero = 6

if numero % 2 == 0:
    print("O número é par")   # % calcula o resto da divisão. Se for 0, é par.

valor = 10
valor2 = 20

if valor < valor2:
    print("O valor 1 é menor que o valor 2")

lista = [1, 2, 3]
numero = 2

if numero in lista:
    print("O número 2 está na lista")   # Verifica se o número está presente na lista

# Aula 2 - else
numero = 11

if numero % 2 == 0:
    print("É par")
else:
    print("É ímpar")  # Será impresso pois 11 é ímpar

idade = 27

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é MENOR de idade")

# Comentado com aspas triplas (multilinha), ótimo para testes sem apagar código
'''
valor = int(input("Digite um número positivo: "))

if valor > 0:
    print(f"O valor {valor} é positivo!")
else:
    print("Você digitou um número negativo")
'''

# Aula 3 - elif (else if)

idade = 11

if idade < 13:
    print("Você é uma criança")
elif idade < 18:
    print("Você é adolescente")
else:
    print("Você é adulto")

nota = 6.5

if nota >= 9:
    print("Você foi muito bem!")
elif nota >= 8:
    print("Você foi bem!")
elif nota >= 7:
    print("Você ficou na média")
elif nota >= 6:
    print("Você está de recuperação")
else:
    print("Você foi muito mal, faça aulas de reforço")

# Explicações importantes:
# - Podemos ter só 'if'
# - Não podemos ter 'else' sozinho (deve sempre vir depois de 'if' ou 'elif')
# - Podemos ter 'if' e vários 'elif' sem 'else'
# - Podemos ter quantos 'elif' quisermos
# - 'else' é opcional, mas recomendado como "último caso"
