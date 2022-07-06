# Aula 14 - Preenchimento de string com zeros utilizando o método format().

print('{:0<5}'.format(25))  # >> 25000
# Veja que o valor 25 foi preenchido com zeros a direita e o total de caracteres agora é 5.

print('{:0>8}'.format(100))  # >> 00000100
# Veja que o valor 100 foi preenchido com zeros a esquerda e o total de caracteres agora é 8.

print('{:#^10}'.format('João'))  # >> ###João###
# Veja que o nome "João" teve ambas laterais preenchidas com # e que o total de caracteres agora é 10.

# Também é possível definir se um valor retornado será exibido como str, int ou float.
x = 100

print('{:0<9}'.format(x))  # >> 100000000

print('{:0>9.5f}'.format(x))  # >> 100.000000
# Veja que no exemplo acima, que após o ponto, foi definido a exibição de cinco casas decimais do valor formatado (float).





