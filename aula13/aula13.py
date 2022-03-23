'''Métodos isdecimal(), isdigit() e isnumeric() são funções que irão checar se uma str pode ou não ser convertida para um int ou float. Ambas as três irão retornar o mesmo valor '''


num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

print(num_1.isnumeric()) #Retornará True se o valor de num_1 for um valor numérico (0-9)

print(num_1.isdecimal()) #Retornará True se o valor de num_1 for um valor decimal (0-9)

print(num_1.isdigit()) #Retornará True se o valor de num_1 for um digit.

if num_1.isnumeric() and num_2.isnumeric():

    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
else:
    print('Digite um número de 0-9')
