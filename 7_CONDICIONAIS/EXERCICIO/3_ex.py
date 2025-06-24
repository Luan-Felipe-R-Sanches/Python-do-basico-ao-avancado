# Exercício 3:
# Enunciado: Desenvolva um sistema de classificação de notas. O programa deve receber uma nota e
# exibir "Aprovado com distinção" para notas maiores ou iguais a 9, "Aprovado" para notas entre 7
# e 8.9, e "Reprovado" para notas abaixo de 7. Utilize operadores ternários.
# Descrição: O programa deve classificar e exibir o status de aprovação com base na nota fornecida,
# usando lógica simplificada.

nota = 9

status = (
    "Aprovado com distinção" if nota >= 9 else
    "Aprovado" if nota >= 7 else
    "Reprovado"
)
