# EXERCÍCIO 1: Criando e manipulando um dicionário de alunos
# DESCRIÇÃO: Crie um dicionário para armazenar nomes de alunos como chaves e suas notas como valores.
# Adicione três pares chave-valor ao dicionário, remova um aluno usando a chave e exiba o restante
# dos pares no dicionário formatados
alunos = {"Ana": 9.0, "Matheus": 7.0, "Rodrigo": 8.0}

alunos["Daniela"] = 7.5

print(alunos)

alunos.pop("Matheus")

print(alunos)