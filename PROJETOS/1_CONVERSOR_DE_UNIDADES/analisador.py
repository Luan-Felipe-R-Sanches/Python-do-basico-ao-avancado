# Receber um texto
# E determinar quantas: palavras, caracteres e linhas o texto tem

def analisar_texto(texto):
    # Quebra o texto em linhas usando splitlines()
    linhas = texto.splitlines()
    numero_linhas = len(linhas)

    # Quebra o texto em palavras usando split() (separa por espaço por padrão)
    palavras = texto.split()
    numero_palavras = len(palavras)

    # Conta todos os caracteres (incluindo espaços e quebras de linha)
    numero_caracteres = len(texto)

    # Retorna os 3 resultados
    return numero_linhas, numero_palavras, numero_caracteres


def main():
    print("Bem-vindo ao Analisador de Textos!")
    print("Digite o seu texto abaixo, e para finalizar pressione Enter duas vezes")

    texto = ""
    while True:
        linha = input()
        # Se a linha estiver vazia, encerra a entrada
        if linha == "":
            break
        texto += linha + "\n"  # Adiciona a linha ao texto, incluindo quebra de linha

    # Chama a função para analisar o texto
    linhas, palavras, caracteres = analisar_texto(texto)

    # Exibe os resultados da análise
    print("Resultado da análise:")
    print(f"Linhas: {linhas}")
    print(f"Palavras: {palavras}")
    print(f"Caracteres: {caracteres}")


# Garante que o programa só rode se for executado diretamente
if __name__ == "__main__":
    main()
