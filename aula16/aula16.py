'''while em Python - aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira.

requisitos - entender condições e operadores.


'''

'''O laço While verifica se uma condição é verdadeira, que no exemplo abaixo é explicitamente verdadeira, e enquanto essa condição for verdadeira, o bloco de códigos será aplicado.'''

'''while True: # Loop infinito
    nome = input('Qual seu nome? ')
    print(f'Olá, {nome}')

print('Não será executada') # --> Essa linha de código não será aplicada.'''

'''Após o interpretador terminar de ler a última linha de código do bloco, ele irá checar novamente a mesma condição, que caso continue sendo verdadeira, irá novamente aplicar o bloco de códigos, criando um loop infinito que só deverá cessar caso a condição se torne falsa.'''



'''x = 0 

while x < 10:
    if x == 3:
        x = x + 1
        break
    print(x)
    x = x + 1

print('Acabou!')  '''


'''x = 0 

while x < 5:
    y = 0

    while y < 5:
        print(f'({x},{y})')
        y = y + 1

    x += 1'''

while True:
    print()
    num_1 = input(f'Digite um número: ')
    num_2 = input(f'Digite outro número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print(f'Por favor, digite um número.')
        continue

    operador = input(f'Digite um operador (+, -, *, /): ')

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
            print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else: 
        print(f'Digite um dos operadores')