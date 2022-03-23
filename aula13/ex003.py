numero = input('Digite um número interno (Ex:1,2,3...): ')





if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O {numero} é um número par.')
    else:
        print(f'O {numero} é um número impar.')
else: 
    print('Digite um número interno.')