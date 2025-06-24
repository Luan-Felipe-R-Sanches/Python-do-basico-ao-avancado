# Aula 1 - break

for numero in range(1, 50):
    print("Numero: ", numero)
    
    if numero % 7 == 0:
        print("Encontramos o numero ", numero)  # Para no primeiro múltiplo de 7
        break

# Loop até o usuário digitar "sair"
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando.lower() == 'sair':
        print("Encerrando programa...")
        break
    print(comando)

frutas = ['maçã', 'banana', 'uva', 'laranja']

for fruta in frutas:
    print(fruta)

    if fruta == 'uva':
        print("Encontramos a uva...")  # Para quando encontrar "uva"
        break

# Aula 2 - continue

numeros = [1, -3, 4, -5, 9, -2]

for numero in numeros:
    if numero < 0:
        continue  # Pula números negativos
    print("O numero é ", numero)

texto = "Python3.12348"

for letra in texto:
    if not letra.isalpha():
        continue  # Pula caracteres que não são letras
    print("Letra: ", letra)

for numero in numeros:
    if numero % 2 == 0:
        continue  # Pula números pares
    print(numero)

# break encerra o loop
# continue pula para a próxima iteração

print("aula 3")

# Aula 3 - combinação de break e continue

for numero in range(1, 20):
    if numero % 2 != 0:
        continue  # Pula ímpares
    if numero % 5 == 0:
        print(f"Primeiro numero divisivel por 5: {numero}")  # Para no primeiro par divisível por 5
        break
    print(numero)

for numero in numeros:
    if numero < 0:
        continue  # Pula negativos
    elif numero > 5:
        print("Numero maior que o previsto, parando loop...")  # Para se for maior que 5
        break
    print(numero)
