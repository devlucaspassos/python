'''
OPERADORES LÓGICOS AND, OR E NOT(inversor), IN e NOT IN.
'''

#O operador AND funciona como um "e", e sendo utilizada, cria um dependencia entre as comparações.

from ctypes.wintypes import PINT


a = 2
b = 2
c = 3 

print(a == b and b < c) # O interpretador vai verificar ambas as comparações.
#Como a comparação a == b e b < c são verdeiras, a saída será True. 
print(a == b and b > c) #A primeira comparação é verdadeira, porém a segunda é falsa. 
#A saída será False, e só será verdadeira, se AMBAS as comparações forem verdadeiras.

#O operador OR funciona como um "ou" e sendo utilizado, não cria dependencia entre comparações.
print(a == b or b > c)#A primeira comparação é verdadeira, porém a segunda é falsa. 
# A saída será True, se uma das duas forem verdadeiras.

#O Operador NOT (inversor) vai inverter os valores.

a = 2
b = 3

if not b > a: 
    print('B é maior que A') 
    '''
    A comparação acima é verdadeira, pois 2 é menor (<) que 3, porém, com a utilização do operator NOT, os valores são invertiso, logo a se torna 3 e b se torna 2, fazendo com que a comparação se torne falsa.
    '''
else:
    print('A é maior que B')


'''Operadores IN e NOT IN (Operadores de Associação) servem para '''

nome = 'Lucas Passos'

#Nesse exemplo, quero saber se existe a letra "i" nesse nome.

if 'i' in nome :
    print('Existe a letra i no nome Lucas Passos')
else:
    print('Não existe a letra i no nome Lucas Passos')

#Outro exemplo 

if 'uca' in nome:
    print('Existe "uca" no nome Lucas Passos') #Verdadeiro (True)


if 'Luc' not in nome: #O operador NOT IN é o inversor do operador IN.
    print('Existe "Luc" no nome Lucas Passos')
else:
    print('Não existe "Luc" no nome Lucas Passos') 
    '''A comparação acima seria verdadeira, pois existe "Luc" em Lucas, mas o operador NOT IN inverteu a compração.'''

#EXEMPLO DE VERIFICADOR DE LOGIN E SENHA

login = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

usuario_bd = 'josilva6'
senha_bd = 'Jo01011978'

if login == usuario_bd and senha == senha_bd:
    print('Login realizado com sucessor')
else:
    print('Não foi possível realizar o login')