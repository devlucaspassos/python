from traceback import print_tb

# Aula 25 -  Operadores ternários
logged_user = False # --> Se usuário está logado ou não.

'''
if logged_user:
    msg = 'O usuário está logado.'
else:
    msg = 'O usuário não está logado.'

print(msg)'''
'''
msg = 'O usuário está logado.' if logged_user else 'O usuário não está logado.'

print(msg)'''
'''
idade = int(input('Digite sua idade: '))
idade_min = 18 

if idade >= idade_min:
    msg = 'O usuário é maior de idade.'
else:
    msg = 'O usuário é menor de idade.'

print(msg)'''

idade = int(input('Digite sua idade: '))
idade_min = 18 

msg = 'O usuário é maior de idade.' if idade >= idade_min else 'O usuário é menor de idade.'

print(msg)