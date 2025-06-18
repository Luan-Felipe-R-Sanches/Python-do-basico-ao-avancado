# Aula 1 - Métodos de String

# Formatação de texto: transforma a string em maiúsculas, minúsculas, etc.
texto = "Python é muito legal"

print(texto.upper())      # Converte todos os caracteres para maiúsculo
print(texto.lower())      # Converte todos para minúsculo
print(texto.capitalize()) # Apenas a primeira letra em maiúsculo

# Remoção de espaços em branco nas extremidades
espacos = " teste aqui de python               "
espacos_limpos = espacos.strip()  # Remove espaços antes e depois
print(espacos)
print(espacos_limpos)

# Substituição de parte do texto
print(espacos.replace("python", "php"))  # Substitui "python" por "php"

# Separação de string com delimitador
dados = "nome,telefone,endereco"
dados_separados = dados.split(",")  # Divide a string em lista usando vírgula
print(dados_separados)

# Aula 2 - split

frase = "Python é muito divertido"
list_frase = frase.split()  # Divide usando espaço como padrão
print(list_frase)
print(list_frase[1])  # Acessa o segundo item da lista resultante

string_caracteres = "teste-testando-testou"
print(string_caracteres.split("-"))  # Divide usando "-" como separador

# maxsplit limita o número de divisões (a partir da esquerda)
print(frase.split(" ", 1))  # Apenas 1 divisão (retorna 2 partes)

# Aula 3 - join

palavras = ["Python", "é", "Incrível"]
print(" ".join(palavras))  # Junta as palavras com espaço
print(",".join(palavras))  # Junta com vírgula

numeros = [1, 2, 3]
# map(str, numeros) transforma todos os números em strings antes de usar join
print(" ".join(map(str, numeros)))  # Necessário converter para string antes do join

# Aula 4 - Replace

texto = "Python é ótimo"
print(texto.replace("ótimo", "perfeito"))  # Substitui uma palavra por outra

palavras = "maça laranja maça banana maça"
# Substitui apenas as 2 primeiras ocorrências de "maça"
print(palavras.replace("maça", "teste", 2))

texto = "sei lá @ teste !"
# Substituição encadeada para remover símbolos
print(texto.replace("@", "").replace("!", ""))

# Mostra que o texto original permanece inalterado (replace não altera a string original)
print(texto)
