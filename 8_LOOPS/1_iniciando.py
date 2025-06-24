# Aula 1 - While

contador = 1
while contador <= 5:
    print(f"Contador: {contador}")  # Contagem de 1 a 5
    contador += 1

x = 10
while x > 0:
    print(x)  # Contagem regressiva de 10 a 1
    x -= 1

while True:
    numero = int(input("Digite um numero positivo: "))
    if numero > 0:
        print("Numero positivo")  # Validação até número positivo
        break

senha = ""
while senha != "12345":
    senha = input("Digite a senha: ")  # Verificação de senha
print("Bem vindo ao sistema")

# Aula 2 - for

frutas = ["Maçã", "banana", "Limão"]

for fruta in frutas:
    print(f"Fruta: {fruta}")  # Itera diretamente sobre a lista

for i, fruta in enumerate(frutas):
    print(f"Fruta: {fruta} referente ao indice {i}")  # Acesso ao índice com enumerate

for numero in range(1, 6):
    print(numero)  # Imprime de 1 a 5

for fruta in frutas:
    if "a" in fruta:
        print(f"Fruta {fruta} tem a letra 'a'")  # Filtra frutas que contêm 'a'

# Aula 3 - Range

for i in range(5):
    print(f"i = a {i}")  # De 0 a 4

for i in range(3, 16, 3):
    print(f"I = {i}")  # De 3 a 15, pulando de 3 em 3

for i in range(10, 0, -1):
    print(f"i = {i}")  # Contagem regressiva de 10 a 1

numeros = [10, 20, 30, 40]
for i in range(len(numeros)):
    print(f"i = {i}, acessando array {numeros[i]}")  # Acesso por índice

# Aula 4 - strings, listas e dicionarios

texto = "Python"
for letra in texto:
    print(f"Letra: {letra}")  # Itera sobre cada caractere da string

dados = {
    "nome": "Matheus",
    "idade": 33,
    "esta_trabalhando": True
}

for chave in dados:
    print(f"Chave {chave} - Valor {dados[chave]}")  # Itera sobre as chaves do dicionário

print(dados['nome'])  # Acesso direto a um valor pela chave

for chave, valor in dados.items():
    print(f"{chave} - {valor}")  # Itera sobre chave e valor ao mesmo tempo
