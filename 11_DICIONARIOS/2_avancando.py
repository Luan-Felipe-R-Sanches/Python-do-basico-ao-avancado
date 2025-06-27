# Aula 1 - Iterando em dicionários
produto = {"nome": "Camisa", "preço": 21, "cor": "Preta"}

# Itera pelas chaves
for chave in produto:
    print(chave)
    print(produto[chave])
    if chave == "nome":
        print("O nome do produto é " + produto[chave])

# Itera diretamente pelos valores
for valor in produto.values():
    print(valor)

# Itera por pares (chave, valor)
for chave, valor in produto.items():
    print(f"{chave} - {valor}")

# Aula 2 - Compreensão de dicionários
numeros = [1, 2, 3, 4]

# Cria dicionário com números e seus quadrados
quadrados = {num: num ** 2 for num in numeros}
print(quadrados)

# Filtra pares do dicionário onde o valor é inteiro
filtrar = {chave: valor for chave, valor in produto.items() if isinstance(valor, int)}
print(filtrar)

# Aula 3 - Dicionários aninhados
usuarios = {
    "user1": {"nome": "Matheus", "email": "matheus@gmail.com"},
    "user2": {"nome": "Maria", "email": "maria@gmail.com"},
}

# Acesso direto em dicionários aninhados
print(usuarios["user1"]["email"])
print(usuarios["user2"]["nome"])

# Iteração em dicionários aninhados
for user, info in usuarios.items():
    print(f"Dados do usuario: {user}")
    for key, value in info.items():
        print(f"{key} - {value}")

# Lista de dicionários
usuarios2 = [
    {"nome": "Matheus", "email": "matheus@gmail.com"},
    {"nome": "Maria", "email": "maria@gmail.com"},
]

for user in usuarios2:
    print(f"Dados do usuario: {user}")
    for key, value in user.items():
        print(f"{key} - {value}")

# Aula 4 - Boas práticas

# .get evita erro se chave não existir (retorna None)
id_produto = produto.get("id")
print(id_produto)

# Cria dicionário com chaves iguais e valor padrão
config = dict.fromkeys(["tema", "volume", "brilho"], "Padrão")
print(config)

# .copy cria cópia independente do dicionário
produto_copia = produto.copy()
produto_copia['preço'] = 50  # Alteração não afeta o original

print(produto)
print(produto_copia)
