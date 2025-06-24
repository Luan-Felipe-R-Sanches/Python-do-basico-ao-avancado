def tabuada():
    print("Bem vindo a tabuada!")

    try:
        # Solicita o número para usuario
        numero = int(input("Digite o número da tabuada: "))

        print(f"Exibindo a tabuada do número {numero}")

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Por favor, insira um número válido.")


if __name__ == "__main__":
    tabuada()
