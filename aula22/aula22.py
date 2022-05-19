'''
split, join e enumerate em Python
split - divide uma string - str
join - juntar uma lista 
Enumerate enumerar elementos de uma lista # list / iteráveis
'''
'''
string = 'O Brasil é o país do futebol, o Brasil é  penta.'

lista_1 = string.split()
lista_2 = string.split('')

print(lista_2)'''
'''string = 'O Brasil é penta'

lista = string.split()

string_2 = ' '.join(lista)
print(string_2)
''' 
'''
string = 'O Brasil é penta.'
lista = string.split()

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])'''


'''
* Enumerate - Enumerar elementos da lista - # list
'''


# -->     
import enum


lista = [ 
#      1       2        3
    ['Edu', 'Lucas', 'João'], #0
#      1       2        3 
    ['Rafa', 'Maria', 'Bianca'], #1
#      1       2        3
    ['Jorge', 'Matheus', 'Luzia'] #2
    ]


enumerada = list(enumerate(lista))


#print(enumerada[1][1][1])
# ->
'''[(0, ['Edu', 'Lucas', 'João']), (1, ['Rafa', 'Maria', 'Bianca']), (2, ['Jorge', 'Matheus', 'Luzia'])]'''

for v1 in enumerada:
 valor_enumerado, valor_lista = v1 
 nome_1, nome_2, nome_3 = valor_lista

 print(nome_2)