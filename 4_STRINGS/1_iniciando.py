# Aula 1 - String
linguagem = "Python"
versao = "3.12"
teste = 'texto'
testando = '''texto'''  # Aspas triplas também definem strings, útil para múltiplas linhas

print(linguagem, versao, teste, testando)

# Concatenação de strings usando o operador +
print("Este é um curso de " + linguagem + ", ele é muito completo!" + teste)

# Repetição de string com operador *
repeticao = "Olá" * 3
print(repeticao)

# Comparação de strings (retorna True/False)
print(linguagem == "Python")

# len() retorna o número de caracteres
print(len("Algum texto"))
print(len(linguagem))

frase = "O curso de Python é muito Bom!"

# Verifica se "Python" está contido na string (retorna True/False)
print("Python" in frase)

# Aula 2 - Indexação
palavra = "Python"

# Acesso a caracteres por índice
print(palavra[0])  # Primeiro caractere
print(palavra[5])  # Último caractere (por índice positivo)
print(palavra[-1])  # Último caractere (por índice negativo)

try:
    print(palavra[11])  # Índice fora do intervalo da string
except IndexError:
    print("Indixe inexistente")  # Tratamento do erro evita crash do programa

# Verifica prefixo e sufixo
print(palavra.startswith("Py"))  # Verifica se começa com "Py"
print(palavra.startswith("on"))
print(palavra.endswith("on"))  # Verifica se termina com "on"

texto = "Esta é uma frase muito grande"

# Fatiamento: retorna parte da string a partir do índice 10 até o final
nova_frase = texto[10:]
print(nova_frase)

# Aula 3 - Fatiamento

frase = "Aprenda a Programar com Python"

# Pega os 7 primeiros caracteres (índice final exclusivo)
subfrase = frase[:7]
print(subfrase)

# Últimos 6 caracteres da string
print(frase[-6:])

# Fatiamento com passo: pega a cada 2 caracteres
print(frase[::2])

# Inverte a string inteira
print(frase[::-1])

# Fatiamento com fim além do comprimento (sem erro)
print(frase[5:100])

# Índice final exclusivo: pega do início até o índice 6
print(frase[:7])
