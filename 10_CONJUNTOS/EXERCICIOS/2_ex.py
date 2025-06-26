# Exercício 2:
# Enunciado: Defina dois conjuntos de palavras representando conjuntos de interesses diferentes. 
# Realize operações de união, interseção e diferença entre eles, exibindo os resultados.
# Descrição: O programa deve criar dois conjuntos de palavras e usar operações matemáticas para 
# calcular união, interseção e diferença.

# Conjuntos com áreas/tecnologias
c1 = {"Python", "IA", "Machine Learning"}
c2 = {"Análise de Dados", "Automação", "Django", "Pandas", "Python"}

# União: elementos presentes em c1 ou c2 (ou ambos)
print(f"União {c1 | c2}")  # Usa operador | para união entre conjuntos

# Interseção: elementos presentes em ambos os conjuntos
print(f"Interseção {c1 & c2}")  # Uso do operador & para obter itens em comum

# Diferença: elementos que estão em c1 mas não em c2
print(f"Diferença {c1 - c2}")  # Útil para saber o que é exclusivo de c1
