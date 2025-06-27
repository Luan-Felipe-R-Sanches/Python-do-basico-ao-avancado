# EXERCÍCIO 3: Iterando sobre dicionários para exibir informações
# DESCRIÇÃO: Crie um dicionário com informações de um funcionário, incluindo nome, cargo e salário. 
# Use um loop for para iterar sobre o dicionário e exibir as informações formatadas chave por valor.

func = {"nome": "Maria", "cargo": "Gerente", "salario": 5000.00}

for chave, valor in func.items():
    print(f"{chave.capitalize()}: {valor}")