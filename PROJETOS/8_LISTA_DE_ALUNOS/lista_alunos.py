def comparar_listas(lista1, lista2):
    
    conj1 = set(lista1)
    conj2 = set(lista2)
    
# interseção, Diferença, Diferença Inversa, Diferença simétrica
    em_ambas = conj1 & conj2
    somente_lista1 = conj1 - conj2
    somente_lista2 = conj2 - conj1
    em_uma_ou_em_outra = conj1 ^ conj2
    
  print("--- Comparação de Listas ---")
  print(f"Alunos em ambas as listas: {em_ambas}")
  print(f"Alunos somente na primeira lista: {somente_lista1}")
  print(f"Alunos somente na segunda lista: {somente_lista2}")
  print(f"Alunos que estão em apenas uma das listas: {em_uma_ou_em_outra}")

def main():
    
    print("Bem-vinfo ao programa de Comparação de lista de Alunos")
    print("Digite os nomes dos alunos, e os separe por virgula")
    
    # Criando as listas
    lista1 = input = input("Digite os nomes da primeira lista: ").split(",")
    lista2 = input("Digite os nomes da segunda lista: ").split(",")
    
    # Remove os espaço em branco
    lista1 = [aluno.split() for aluno in lista1]
    lista2 = [aluno.split() for aluno in lista2]
    
    print(lista1)
    print(lista2)
    
