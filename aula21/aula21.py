'''
for / else em Python.
'''

'''variavel = ['joão', 'Maria', 'Betinho']'''

'''for valor in variavel:
    if valor.startswith('J'):
        print(f'O nome {valor} começa com a letra J.')
    else:
        print(f'O nome {valor} não começa com a letra J.')'''

'''for valor in variavel:
    if valor.lower().startswith('j'):
        letra_J = True

if letra_J:
    print('Existe uma palavra que começa com a letra J.')
else:
    print('Não existe palavras que começam com a letra J.')'''

variavel = ['joão', 'Maria', 'Betinho']

for valor in variavel:
    if valor.lower().startswith('j'):
        print('Contém um ou mais nomes que começam com a letra "J".')
        break
else:
    print('Não há nomes que começam com a letra "J".')
