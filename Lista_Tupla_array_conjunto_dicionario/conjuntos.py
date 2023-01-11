"""
vamos trabalhar agora com conjuntos, quando falamos de SET estamos falando das propriedades matematicas de um conjunto
sua utilizadade é exatamente essa.

O Python também inclui um tipo de dados para conjuntos . Um conjunto é uma coleção não ordenada sem elementos
duplicados. Os usos básicos incluem testes de associação e eliminação de entradas duplicadas. Objetos de conjunto
também suportam operações matemáticas como união, interseção, diferença e diferença simétrica.

As chaves ou a set()função podem ser usadas para criar conjuntos. Nota: para criar um conjunto vazio você deve usar
set(), not {};


"""
conjunto_pares = []
k = 0
for i in range(0, 100):
    conjunto_pares.append(k)
    k += 2

conjunto_impares = []
k = 1
for i in range(0, 100):
    conjunto_impares.append(k)
    k += 2

conjunto_primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 21, 23]

print(conjunto_pares)
print(conjunto_impares)
print(conjunto_primos)
print("---------------------------------------------------------------")

conjunto_total = []
conjunto_total.extend(conjunto_impares)
conjunto_total.extend(conjunto_pares)
conjunto_total.extend(conjunto_primos)
print(conjunto_total)


conjunto_pares = set(conjunto_pares)
conjunto_impares =set(conjunto_impares)
conjunto_primos = set(conjunto_primos)
conjunto_total = set(conjunto_total)

print("--------------------------------------------------------------------------------------")
print(conjunto_pares)
print(conjunto_impares)
print(conjunto_primos)
print(conjunto_total)
'''
não se pode acessar um conjunto como se fossse uma lista 
print(conjunto_total[1])
'''

'''
operações de conjuntos
| uniao --> letters in a or b or both
& intersecção --> letters in both a and b
- diferença --> letters in a but not in b
^ ou exclusivo --> letters in a or b but not both
'''

print('resultados de operações ')
print(conjunto_impares | conjunto_pares)
print(conjunto_impares & conjunto_primos)
print(conjunto_total - conjunto_impares)
print(conjunto_impares ^ conjunto_primos)

'''
ainda podemos congelar um conjuto fazendo dele um conjunto imutavel 
e podemos adicionar ou deletar elementos nos conjuntos 
'''
frozenset(conjunto_total)
conjunto_primos.add(0)