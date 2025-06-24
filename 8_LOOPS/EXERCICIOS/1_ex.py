# Exercício 1:
# Enunciado: Escreva um programa que utilize um loop `while` para solicitar ao usuário números
# inteiros até que ele digite um número negativo. Ao final, exiba a soma de todos os números
# inseridos.
# Descrição: O programa deve utilizar um loop `while` para acumular valores em uma variável,
# interrompendo o loop quando um número negativo for inserido.

# Loop infinito que continuará pedindo números até o usuário digitar um número negativo
while True:
    numero = int(input("Digite um numero inteiro ou negativo para sair do programa: "))

    # Encerra o loop se o número for negativo
    if numero < 0:
        break

    # Soma os números digitados (ERRO: a variável 'soma' não foi inicializada antes do uso)
    soma += numero

# Exibe o resultado final da soma
print(f"A soma é: {soma}")