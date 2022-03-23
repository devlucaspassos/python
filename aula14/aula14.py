#Usando o .:(Número de casas decimais.)f 

from math import radians


num_1 = 3
num_2 = 10 

divisao = num_2 / num_1 # O resultado é 3.333333333...

print('{:.2f}'.format(divisao)) #Exibe somento duas casas decimais (ex:3.33)

print('{:.2f}'.format(5.2131)) #Vai exibit 5.21



nome = 'Lucas'

print(f'{nome:s}') 

'''Preenchemento com zaros (): Usando esse método de formatação, você preenche com zeros(0) um certo valor, e ainda escolhendo qual direção esses zeros irão ser exibidos, sendo essas posições definizar pelos operadores (> esquerda, < direita e ^ centro.). Esse preenchemento vai fazer com que o número total de caracteres seja igual ao número inserido após o operador. Por exemplo: :0<7 faz com que o valor formatado seja preenchido com zeros a deireita até que o total de caracteres seja 7.'''

#Preenchemento com zeros a esquerda (>)

print('{:0>9}'.format(21.5))#Preenche a parte esquerda do valor com zaros até totalizar 9 caracteres
#Retornará: 00000021.5, pois foram adicionados 5 zeros, somando um total de 9 caracteres.

print('{:0>7}'.format(99.9))#Preenche com zeros na direção esquerda até ter um total de 7 caracteres

#preenchemento com zeros a direita (<)

print('{:0<5}'.format(15))#Preenche com zeros a direra (Rotornará: 15000)

print('{:0<8}'.format(666))#Preenche com zeros a direita (Retornará: 660000000)

#Por o número no centro (^)
'''o operador ^ faz com que o número seja centralizado e as laterais preenchidas com zeros'''
print(f'{199:0^10}') #O valor retornado será 0001990000, veja que o número "199" foi centralizado e ambas as direções direita e esquerda foram preenchidas com zeros.

#Também é possível fazer a combinação des métodos como por exemplo:

num_x = 123

print(f'{num_x:0>9.2f}') 
#O valor exibido será 000123.00

#Também dá para formatar strings 

print(f'{nome:#^11}') #Saída: ###Lucas###
'''
No exemplo acima, a variável nome foi centralizada (^), além de ser sido preenchida com cerquilhas (#) até que o valor tivesse um total de 11 caracteres.
'''






