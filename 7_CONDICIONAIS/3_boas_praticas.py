# Aula 1 - condicionais em processamento de dados
dados = [10, -5, 8, 0, -1]

# List comprehension com condicional
# Cria nova lista apenas com números maiores que 0
dados_validos = [x for x in dados if x > 0]

print(dados_validos)  # Saída: [10, 8]

idades = [10, 15, 20, 23, 12, 18, 44, 60]

# Categoriza cada idade com base em faixas etárias
categorias = [
    "Criança" if idade < 13 else "Adolescente" if idade < 18 else "Adulto"
    for idade in idades
]

print(categorias)

idade = 20
maioridade = 18

# Avaliação booleana direta
maior_de_idade = idade >= maioridade

print(maior_de_idade)  # True

# hard coded = quando o dado é escrito pelo dev, não vem de uma variável ou banco de dados
