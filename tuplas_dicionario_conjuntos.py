#LISTAS !!!

#empty list
lista =[]

#creating a list with for
lista = [i for i in range(11)]
print(type(lista))
print(lista)


#TUPLAS !!!

# is not possible to append, remove or modify elements in a tuple

#empty tupla
tupla = ()
tupla = (0,1,2,3,4)

#is necessary write "tuple" like a "int" or "str" convertion
tupla_create = tuple([i for i in range(11)])

print(type(tupla))
print(tupla)
print(type(tupla_create))
print(tupla_create)

# CONJUNTOS (sets)!!!

#empty set is a dict
conjunto_vazio = {}
print(type(conjunto_vazio))

#sets not accept duplicates
conjunto = {1,2,3,4,5,6,2,4,5}
print(type(conjunto))
print(conjunto)

#conjuntos não são ordenados
conjunto2 = {"a","b","c","d","e"}
print(type(conjunto2))
print(conjunto2)

#possui operações de conjuntos matematicos


