'''
Desempacotamento de listas em Python
'''
'''
lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)'''

'''a, b, c = 'DIA' # --> "a" = "D", "b" = "I", "c" = "A"

print(a) # --> Retornará: D

print(b) # --> Retornará: I

print(c) # --> Retornará: A'''

'''a, b, c = [1, 2, 3] # --> "a" = "1", "b" = "2" e "c" = "3"

print(a) # --> Retornará: 1

print(b) # --> Retornará: 2

print(c) # --> Retornará: 3'''


a, b, *c = [1, 2, 3, 4, 5] # --> "a" = "1", "b" = "2" e "c" = "3", "4" e "5"

print(a) # --> Retornará: 1

print(b) # --> Retornará: 2

print(c) # --> Retornara: [3, 4, 5]






