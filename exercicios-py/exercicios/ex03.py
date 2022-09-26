'''
3º Exercício
    Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
'''

num = int(input('Digite um número inteiro para saber sua tabuada: '))

print(f'Veja abaixo a tabuada de {num}.')

for n in range(11):
    print(f'{num} x {n} é igual a {num * n}.')



