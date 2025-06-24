def calcular_imc():
    print("Bem-vindo à calculadora de IMC!")

    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

    # Calcular o IMC
    imc = peso / (altura ** 2)

    print(f"Seu IMC é {imc:.2f}")

    # Exibir a categoria do usuário
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    elif imc < 34.9:
        print("Classificação: Obesidade grau 1")
    elif imc < 39.9:
        print("Classificação: Obesidade grau 2")
    else:
        print("Classificação: Obesidade mórbida")

if __name__ == "__main__":
    calcular_imc()
