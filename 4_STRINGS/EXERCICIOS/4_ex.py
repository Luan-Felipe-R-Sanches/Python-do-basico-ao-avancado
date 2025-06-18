# Exercício 4:
# Enunciado: Crie uma string multilinha com uma mensagem de boas-vindas que inclua variáveis
# como o nome do usuário e a data atual, formatada com f-strings.
# Descrição: O programa deve usar uma string multilinha com aspas triplas e incluir variáveis
# formatadas dinamicamente com f-strings para exibir uma mensagem personalizada.

from datetime import date  # Importa apenas a classe date do módulo datetime

nome_usuario = input("Digite o seu nome: ")  # Entrada do nome do usuário

# Obtém a data atual e formata como dia/mês/ano (ex: 18/06/2025)
data_atual = date.today().strftime("%d/%m/%Y")

# f-string multilinha com interpolação de variáveis
mensagem = f'''
    Bem-vindo {nome_usuario}!
    Hoje é {data_atual}
    '''
