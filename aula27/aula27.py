# função def em Python

# 1 -  Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
'''
def ola(saudacao, nome):

    print(f'{saudacao}, {nome}.')

ola('Oi', 'Lucas')
'''
# 2 - Crie uma função que receba três números e exiba a soma dos três.
'''
def soma(a, b, c):

    x = a + b + c
    print(x)

'''
 #3 - Crie uma função que receba dois números inteiros. O primeiro é o valor e o segundo é o percentual (ex:10%). Retorne (return) o valor do primeiro somado do aumento do percentual do mesmo.
'''
def soma_percentual(x, y):

    y = x * y / 100
    soma = x + y
    return soma

sp = soma_percentual(4550, 13.5)
print(sp)
'''
# 4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne Fizz. Se o parâmetro for divisível por 5, retorne Buzz. Se o parâmetro da função for divisível por 3 e 5, retorne Fizz Buzz.


def fizzbuzz(x):
    if  x % 3 == 0 and x % 5 == 0:
        return 'Fizz Buzz'
    if x % 5 == 0:
        return 'buzz'
    if x % 3 == 0:
        return 'fizz'
    return x

fbz = fizzbuzz(15)
print(fbz)
