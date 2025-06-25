# Função para exibir contatos armazenados na tupla
def exibir_contatos(contatos):
    if not contatos:
        print("A agenda está vazia...")
    else:
        # Percorre a tupla com índice, desempacotando cada contato em nome, telefone e email
        for i, contato in enumerate(contatos, start=1):
            nome, telefone, email = contato
            print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}")

# Função para adicionar um novo contato na tupla de contatos
def adicionar_contatos(contatos):
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu email: ")

    novo_contato = (nome, telefone, email)  # Cria tupla com dados do contato

    return contatos + (novo_contato, )  # Retorna nova tupla concatenada (tuplas são imutáveis)

def main():
    contatos = ()  # Tupla vazia inicial para armazenar contatos

    while True:
        print("Menu de Agenda")
        print("1. Exibir contatos")
        print("2. Adicionar um contato")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Exibindo contatos...")
            exibir_contatos(contatos)
        elif opcao == "2":
            print("Adicionando novo registro...")
            contatos = adicionar_contatos(contatos)  # Atualiza a tupla com novo contato
        elif opcao == "3":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
