# AUla 11 - Operadores lógicos AND, OR E NOT(inversor), IN e NOT IN.

# O operador AND funciona como um "e", e sendo utilizada, cria um dependencia entre as comparações.

a = 2
b = 2
c = 3 

# O interpretador vai verificar ambas as comparações.
print(a == b and b < c)  # >> True
# Como a comparação a == b e b < c são verdeiras, a saída será True. 

print(a == b and b > c)  # >> False
# A primeira comparação é verdadeira, porém a segunda é falsa. 
# A saída será False, e a saída só será True, se ambas as comparações forem verdadeiras.

# O operador OR funciona como um "ou" e sendo utilizado, não cria dependencia entre comparações.

a = 2
b = 2
c = 3 

print(a == b or b > c) # >> True
# A primeira comparação é verdadeira, porém a segunda é falsa. 
# A saída será True, se uma das duas forem verdadeiras.

# O Operador NOT (inversor) vai inverter os valores.

a = 2
b = 3

if not b > a:  # O operador NOT inverte os valores de a e b. Tornando a expressão falsa.
    print('B é maior que A')
else:
    print('A é maior que B')  # >> Essa mensagem será exibida.


# Operadores de associação IN e NOT IN.

nome = 'João'

# Nesse exemplo, quero saber se existe a letra "J" no nome "João".

if 'J' in nome:
    print(f'Existe a letra "J" no nome {nome}')
else:
    print(f'Não existe a letra "J" no nome {nome}')

# Outro exemplo da utilização do operador IN. 

cpf = '010.714.350-00'

if '10' in cpf:
    print(f'Existe o número 10 no cpf: {cpf}') 
else:
    print(f'Não existe o número 10 no cpf : {cpf}')

# Exemplo da utilização do operador NOT IN, que é o inversor do operador IN.

nome = 'João'

if 'J' not in nome:  # Utilização do operador NOT.
    print(f'Existe a letra "J" no nome {nome}')
else:
    print(f'Não existe a letra "J" no nome {nome}')  # >> Mensagem que será exibida.
