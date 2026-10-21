import random
from turmas import turma307 as turma


# Função para dividir a lista em n grupos aleatórios
def dividir_em_grupos(lista, n_grupos):
    random.shuffle(lista)  # Embaralha a lista original
    return [lista[i::n_grupos] for i in range(n_grupos)]


grupos = dividir_em_grupos(turma, 3)

print("Turma 307")
print("--------------------------------")
# Exibindo os grupos
for i, grupo in enumerate(grupos, 1):
    print(f"Grupo {i}:")
    print(grupo)
    print()