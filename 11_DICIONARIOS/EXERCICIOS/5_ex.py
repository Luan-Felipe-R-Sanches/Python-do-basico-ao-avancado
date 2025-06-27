# EXERCÍCIO 5: Trabalhando com dicionários aninhados para organização de dados
# DESCRIÇÃO: Crie um dicionário aninhado para armazenar informações de clientes. Cada cliente deve 
# ter um identificador único e conter informações como nome, idade e cidade. Exiba os dados de 
# cada cliente formatados em linhas separadas.

clientes = {
    "cliente1": {"nome": "Carlos", "idade": 30, "cidade": "São Paulo"},
    "cliente2": {"nome": "Mariana", "idade": 25, "cidade": "Rio de Janeiro"},
    "cliente3": {"nome": "Pedro", "idade": 28, "cidade": "Belo Hrizonte"},
}

for cliente, dados in clientes.items():
    print(f"{cliente.capitalize()}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()} - {valor}")