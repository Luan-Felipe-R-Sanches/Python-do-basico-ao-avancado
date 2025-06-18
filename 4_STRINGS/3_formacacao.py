# Aula 1 - f-string (forma moderna e legível de formatar strings)

nome = "Matheus"
idade = 33
print(f"Meu nome é {nome} e eu tenho {idade} anos")  # Interpolação direta de variáveis

a = 5
b = 10
print(f"A soma de {a} e {b} é igual a {a + b}")  # Expressões podem ser usadas dentro da f-string

valor = 12.9892754
print(f"O valor arredondado é {valor:.2f}")  # Formatação de float com 2 casas decimais

# Aula 2 - format()

print("Meu nome é {} e eu tenho {} anos".format("Aline", 23))  # Substituição por posição

valor = 1.2345
print("O valor formatado é {:.3f}".format(valor))  # Formatação com 3 casas decimais

print("Ordem de parâmetros invertida {1} e {0}".format("primeiro", "segundo"))  # Alterando ordem com índice

# Aula 3 - String multilinha

texto = """Este é meu
texto com multilinha"""  # Texto com quebras de linha automáticas
print(texto)

nome = "Luan"
frase = f"""Meu nome é
{nome}
tudo bem?"""  # f-string também pode ser usada com multilinhas
print(frase)

texto_com_escape = """
Qualquer coisa
\n\n
pulou linha"""  # \n será interpretado como texto literal aqui
print(texto_com_escape)

# Aula 4 - Caracteres especiais

texto = "Testando \n Caracteres \n Especiais"  # \n cria quebras de linha reais
print(texto)

aspas = "E quero \"colocar\" aspas"  # Aspas duplas escapadas dentro de string com aspas duplas
aspas2 = 'E quero "colocar" aspas'  # Alternativa: usar aspas simples fora
print(aspas)

# r (raw string) evita que caracteres de escape sejam processados
caminho_de_uma_pasta = r"C:\Users\Matheus\Teste.txt"
print(caminho_de_uma_pasta)  # Útil para caminhos no Windows ou expressões regulares
