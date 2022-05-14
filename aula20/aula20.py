'''
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend,+ 
min, max
range
'''
'''#Índices: 0    1    2    3    4    5 (Positivos)

lista = ['A', 'B', 'C', 'D', 'E', 10.1]

#Índices:-6   -5   -4   -3   -2   -1 (Negativos)

lista[2] = 'Banana'

print(lista[2])'''



'''l1 = [1, 2, 3]

l1.append('AAA')

print(l1) # --> Retornará: [1, 2, 3, 'AAA']'''



'''l1 = ['B', 'C', 'D']
l1.insert(0, 'A')

print(l1) # --> Retornará: ['A', 'B', 'C', 'D']
'''

'''l1 = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
print(l1) # --> Retornará

l1.pop(2)

print(l1) # -- Retornará: ['Banana', 'Morango'] 
'''
'''
#Índices:  0    1    2    3    4    5    6    7    8

l1 =     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

print(l1) # --> Retornará: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

del(l1[3:6])

print(l1) # --> Retornará: ['A', 'B', 'C', 'G', 'H', 'I'] 
'''

'''frutas = ['Abacate', 'Banana', 'Caju']

print(frutas) # --> Retornará: ['Abacate', 'Banana', 'Caju']

del(frutas[0])

print(frutas) # --> Retornará: ['Banana', 'Caju'] '''


'''
l1 = [1, 3, 4, 5, 6, 7, 8, 9]

print(min(l1)) # --> Retornará: 1
print(max(l1))# --> Retornará: 9

l2 = ['A', 'B', 'C', 'D', 'E']

print(min(l2)) # --> Retornará: A
print(max(l2)) # --> Retornará: E
'''



'''l1 = ['string', True, 10, 20.5]

for elem in l1:
    print(f'O tipo de {elem} é {type(elem)}')'''


'''l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0

for valor in l2:
    soma = soma + valor

print(soma)'''


















