# Aula 1 - Condicionais aninhadas

idade = 22

if idade >= 18:
    print("Você é maior de idade")

    if idade >= 21:
        print("Você pode consumir bebida nos EUA")
    else:
        print("Você não pode consumir bebida nos EUA")
else:
    print("Você é menor de idade")

nota = 10

if nota >= 7:
    if nota == 10:
        print("Você tirou a nota máxima!")  # Executa apenas se nota for exatamente 10

    print("Você foi aprovado!")  # Executa se nota >= 7
else:
    print("Você está de recuperação")


lista = [1, 2, 3]

if len(lista) > 0:
    if 2 in lista:
        print("O número 2 está na lista")
        if True:
            print("Muito legal")  # Sempre será executado, pois a condição é True literal
    else:
        print("O número 2 NÃO está na lista")
else:
    print("A lista está vazia")

# Aula 2 - Combinação de condições e operadores lógicos

idade = 23
renda = 900

if idade < 30 and renda < 1800:
    print("Você pode participar do programa.")

usuario = 'teste1234'
senha = 'minhasenha'

# Simulação de login (credenciais incorretas)
if usuario == 'teste123' and senha == 'minhasenha':
    print("Você logou no sistema")
else:
    print("Credenciais erradas")
    
    x = 11
y = 20
z = 20

# Atenção à precedência dos operadores: 'and' tem prioridade menor que 'or'
if (x < y or y < z) and x == 10:
    print("Condição verdadeira")
else:
    print("Deu errado")

if x < y or y < z and x == 10:
    print("Condição verdadeira")
else:
    print("Deu errado")

x = 11
y = 20
z = 20

# Atenção à precedência dos operadores: 'and' tem prioridade menor que 'or'
if (x < y or y < z) and x == 10:
    print("Condição verdadeira")
else:
    print("Deu errado")

if x < y or y < z and x == 10:
    print("Condição verdadeira")
else:
    print("Deu errado")

# x < y => True
# y < z => False
# x == 10 => False
# True or (False and False) => True or False => True
# Portanto, imprime: "Condição verdadeira"

# Aula 3 - Operador ternário (condição curta)

idade = 20

# Versão compacta
resultado = "Maior de idade" if idade >= 18 else "Menor de idade"
print(resultado)

# Versão comum
if idade >= 18:
    resultado = "Maior de idade"
else:
    resultado = "Menor de idade"

numero = 8

# Teste de paridade
paridade = "É par" if numero % 2 == 0 else "Não é par"
print(paridade)

# Fórmula do operador ternário:
# VALOR_IF_TRUE if CONDIÇÃO else VALOR_IF_FALSE

# Aula 4 - Funções e dicionários com condicionais

def verifica_idade(idade):
    if idade < 18:
        return "Menor de idade"
    return "Maior de idade"

print(verifica_idade(16))
print(verifica_idade(26))

# Simulação de semáforo com dicionário
opcoes = {
    "vermelho": "Pare",
    "amarelo": "Atenção",
    "verde": "Siga"
}

cor = input("Digite uma cor (verde, vermelho ou amarelo): ")

# .get() retorna um valor padrão caso a chave não exista
print(opcoes.get(cor, "Cor inválida"))

# Condicional combinada com aninhamento vs direta

idade = 25
renda = 3000

# Forma aninhada
if idade > 18:
    if renda > 2000:
        print("Elegível ao benefício")

# Forma combinada
if idade > 18 and renda > 2000:
    print("Elegível ao benefício")
