# -*- coding: utf-8 -*-

'''
trabalhando com listas.
quando queremos utilizar varias variaveis utilizamos listas, elas são objetos interaveis (__inter__) do python
além de serem objetos interaveis, são objetos modificaveis ou seja seu conteudo e ordem podem ser alterados

a extrutura básica das listas são referenciadas pelos []
'''

#referenciando
idades = [39, 30, 27, 18]

#tipo
print(type(idades))

#tamanho
print(len(idades))

#extraindo informações
print(idades[0])


'''
vamos agor conhecer um pouco das funções listadas na documentação do python 
'''

'''append  --  o metodos adiciona no final da lista o novo componente '''
print('lista antiga' , idades)
idades.append(25)
print('lista nova', idades)
print('novo len',len(idades))

'''extend -- passando um interavel o metodo ira inserir os valores no final da lista'''

idades.extend([11,12,13])
print('lista nova', idades)

'''insert -- o metodo inserie um valor em uma posição determinada'''
idades.insert(2,23)
print('lista nova', idades)

'''remove -- remove o primeiro item da lista com o valor identificado (1,2,1) -- remove(1) -- (2,1) '''
idades.remove(39)
print('lista nova', idades)

'''remove um valor com a possição expecificada e retorna o valor excluido, se a possição não for informada vai excluir 
o ultimo item'''
print(idades.pop(0))

"""Clear ----- exclui todos os intens da lista  == del a[:]."""

idades.clear()
print('lista nova', idades)

idades = [1,2,3,4,45,6,7,8,9,10,11,12,13,14,15]

'''index list.index(x[, start[, end]]) proura o valor e retorna a sua posição na lista, pode se adicionar inicio e fim
 de busca'''

print(idades.index(10))
#print(idades.index(10,0,5))

'''count --- literalmente para contar o numero de item dentro de uma lista'''

idades.extend([22,22,22,22,22])
print(idades)
print(idades.count(22))


'''sort -- modifica a lista de maneira organizada ,,, mas voce pode modificar a maneira de ser sorteado os itens
Sort items of the list in place(the arguments can be used for sort customization, see sorted() for their explanation)
list.sort(*, key=None, reverse=False)
'''
idades.sort()
print(idades)

'''reverse -- inverte a posição dos item '''
idades.reverse()
print(idades)


'''copy ---- copia uma  lista para a outra '''

a = idades.copy()
print(a)

