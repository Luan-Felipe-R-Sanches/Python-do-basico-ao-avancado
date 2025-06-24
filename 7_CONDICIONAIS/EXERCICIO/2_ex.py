# Exercício 2:
# Enunciado: Crie um programa que solicite ao usuário uma senha e verifique se ela atende aos
# seguintes critérios: tem pelo menos 8 caracteres, contém pelo menos um número e uma letra. Use
# condicionais e operadores lógicos.
# Descrição: O programa deve validar a senha com base nos critérios, exibindo mensagens para cada
# caso (válido ou inválido).
# isdigit = é numero
# isalpha = é letra

senha = 'test123'

tem_8_caracteres = len(senha) >= 8

tem_numero = any(char.isdigit() for char in senha)

tem_letra = any(char.isalpha() for char in senha)

if tem_8_caracteres and tem_numero and tem_letra:
    print("Senha forte!")
else:
    print("Senha fraca")