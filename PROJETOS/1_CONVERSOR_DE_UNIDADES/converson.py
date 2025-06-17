# Converter celsius para F
# Converter F para C

# Função para converter de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    # Fórmula: (°C × 9/5) + 32 = °F
    return (celsius * 9/5) + 32

# Função para converter de Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    # Fórmula: (°F − 32) × 5/9 = °C
    return (fahrenheit - 32) * 5/9

# Função que exibe o menu de opções para o usuário
def menu():
    print("Bem-vindo ao Conversor")
    print("Escolha uma opção:")
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    print("3 - Sair")

# Função principal do programa, responsável pela lógica do conversor
def conversor_temperatura():
    menu()  # Exibe o menu
    opcao = input("Digite a opção (1/2/3): ")  # Lê a opção escolhida pelo usuário

    # Se o usuário escolher 1, realiza a conversão de Celsius para Fahrenheit
    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))  # Entrada do usuário
        fahrenheit = celsius_para_fahrenheit(celsius)  # Chamada da função de conversão
        print(f"{celsius:.2f}°C é equivalente a {fahrenheit:.2f}°F")  # Saída formatada com 2 casas decimais

    # Se o usuário escolher 2, realiza a conversão de Fahrenheit para Celsius
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))  # Entrada do usuário
        celsius = fahrenheit_para_celsius(fahrenheit)  # Chamada da função de conversão
        print(f"{fahrenheit:.2f}°F é equivalente a {celsius:.2f}°C")  # Saída formatada

    # Se o usuário escolher 3, encerra o programa
    elif opcao == "3":
        print("Obrigado por utilizar o conversor!")

    # Qualquer outra opção é inválida
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")

# Ponto de entrada do programa
if __name__ == "__main__":
    conversor_temperatura()

