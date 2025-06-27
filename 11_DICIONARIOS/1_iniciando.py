# Aula 1 - Criação de dicionários
dic = {"nome": "Matheus", "idade": 30}

dic2 = dict(cidade="São Paulo", estado="SP", populacao=4742743274)

print(dic)
print(dic2)

dic_vazio = {}
print(dic_vazio)

# Criando dicionário a partir de lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
dic_tuplas = dict(pares)
print(dic_tuplas)

# Aula 2 - Manipulação de dicionários
dic["profissao"] = "Programador"  # Adiciona nova chave
print(dic)

dic["nome"] = "Matheus Battisti"  # Atualiza valor existente
print(dic)

valor_excluido = dic.pop("idade")  # Remove a chave e retorna o valor
print(valor_excluido)
print(dic)

del dic["nome"]  # Remove a chave diretamente
print(dic)

dic.clear()  # Limpa o dicionário completamente
print(dic)

# Adiciona nova chave após limpar
dic["cidade"] = "Rio de Janeiro"
print(dic)

# Aula 3 - Acesso de valores
pessoa = {"nome": "Matheus", "idade": 30, "profissao": "Programador"}

print(pessoa["idade"])  # Acesso direto
print(pessoa.get("teste"))  # Retorna None se chave não existir

# Verificação de existência de chave
if 'teste' in pessoa:
    print("chave existe")
else:
    print("chave NAO existe")

print(len(pessoa))  # Número de pares chave-valor

# Aula 4 - Métodos de dicionário
chaves = pessoa.keys()
valores = pessoa.values()
itens = pessoa.items()

print(list(chaves))   # Lista de chaves
print(list(valores))  # Lista de valores
print(list(itens))    # Lista de tuplas (chave, valor)
