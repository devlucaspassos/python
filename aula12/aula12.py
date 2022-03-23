'''
Função LEN
'''

usuario = input('Digite seu nome de usuário: ')
qtd_caracteres = len(usuario)
qtd_minima = 6

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < qtd_minima:
    print('Insira 6 ou mais caracteres')
else:
    print('Login realizado com sucesso')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite mais alguma coisa: ')

print(f'A soma do número de caracteres das variáveis "input1" e "input2" é: {len(string1) + len(string2)}')


