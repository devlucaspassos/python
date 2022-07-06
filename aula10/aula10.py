# Aula 10 - Operadores relacionais ou operadores de comparação.
# Operadores: == > >= < <= !=


# Igual (==) - Verifica se os valores comparados são iguais.
# Diferente (!=) - Verifica se os valores comparados são diferentes.
# Menor (<) - Verifica se o valor da esquerda é menor que o valor da direita.
# Maior (>) - Verifica se o valor da esquerda é maior que o valor da esquerda)
# Menor igual (<=) - Verifica se o valor da esquerda é menor ou igual ao valor da direita.
# Maior igual (>=) - Verifica se o valor da esquerda é maior ou igual ao valor da esquerda.


# Primeiro exemplo, utilizando variáveis contendo valores inteiros (int).

x = 2
y = 2 
z = 3

print(x == y)  # Essa expressão é verdadeira (True), já que 2 é igual a 2.
print(x == z)  # Essa expressão é falsa (False), pois 2 não é igual a 3.
print(y < z)  # >> True
print(y > x)  # >> False
print(z != y) # >> True

# Segundo exemplo, utilizando variáveis do tipo string.

a = 'pato'
b = 'gato'
c = 'pato'

print(a == c) # >> True
print(a == b)  # >> False

