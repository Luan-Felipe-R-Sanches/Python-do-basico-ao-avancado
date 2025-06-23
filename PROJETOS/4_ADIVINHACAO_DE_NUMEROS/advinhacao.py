import random

def jogo_advinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar um número aleatório de 1 a 100!")
    
    # Gerar o número aleatório
    numero_secreto = random.randint(1, 100)

    # Inicializar variáveis de controle
    tentativas = 0
    acertou = False
    max_tentativas = 10  # Limite opcional

    while not acertou and tentativas < max_tentativas:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns, você acertou o número {numero_secreto} em {tentativas} tentativas!")
            acertou = True
        elif palpite < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")

    if not acertou:
        print(f"Game Over! O número secreto era {numero_secreto}. Você usou todas as {max_tentativas} tentativas.")

# Garante que o jogo só execute se o arquivo for o principal
if __name__ == "__main__":
    jogo_advinhacao()
