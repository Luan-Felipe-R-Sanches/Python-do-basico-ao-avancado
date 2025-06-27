# Sistema de Inventário

def exibir_menu():
    print("--- Sistema de Inventário ---")
    print("1. Adicionar um Produto")
    print("2. Atualizar a Quantidade de um Produto")
    print("3. Consultar o Estoque")
    print("4. Sair")
    return input("Escolha uma opção: ")

def adicionar_produto(inventario):
    produto = input("Digite o nome do Produto: ")

    if produto in inventario:
        print(f"O produto {produto} já está cadastrado...")
    else:
        try:
            quantidade = int(input("Digite a quantidade inicial do produto: "))
            inventario[produto] = quantidade
            print(f"O produto {produto} foi adicionado!")
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")

def atualizar_quantidade(inventario):
    produto = input("Digite o nome do Produto para atualizar: ")

    if produto not in inventario:
        print(f"O produto {produto} não existe...")
    else:
        try:
            quantidade = int(input("Digite a nova quantidade do produto: "))
            inventario[produto] = quantidade
            print(f"O produto {produto} foi atualizado!")
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")

def consultar_estoque(inventario):
    if not inventario:
        print("O estoque está vazio...") 
    else:
        print("-- Estoque Atual ---")
        for produto, quantidade in inventario.items():
            print(f"{produto}: {quantidade} unidades")

def main():
    inventario = {}

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            adicionar_produto(inventario)  # Chama a função para adicionar
        elif opcao == "2":
            atualizar_quantidade(inventario)  # Chama a função para atualizar
        elif opcao == "3":
            consultar_estoque(inventario)  # Chama a função para consultar
        elif opcao == "4":
            print("Encerrando Sistema de Inventário. Até mais!")
            break  # Encerra o laço e o programa
        else:
            print("Opção inválida. Escolha de 1 a 4.")

if __name__ == "__main__":
    main()  # Ponto de entrada do programa
