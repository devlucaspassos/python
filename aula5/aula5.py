'''
---> OPERADORES ARITMÉTICOS
+, -, *, **, /, //, %, () 
'''
import string


print(10 + 10)  # Operador de soma
print(10 - 10)  # Operador de subtração
print(10 * 10)  # Operador de multiplicação
print(10 ** 10)  # Operador de potenciação (Nesse caso vai ser 10 elevado a 10 = 100)
print(10 / 10)  # Operador de divisão
print(10 // 10)  # Operador de divisão inteira (vai arredondar os números)
print(19 % 18)  # Operador módulo (exibe o resto de uma divisão)
print(10 + (20 - 10) * (25 - 15)) # alteração de precendência com os parênteses.

# O operador de multiplicação também pode multiplicar strings, criando uma repetição, veja o exemplo:
print(10 * 'A')

# O operador de soma (+) quando usado entre strings, faz a concatenação (Junção) das mesmas.
print('Lucas' + 'Passos')
#Concatenando mais de duas strings
print('Lucas' + ' ' + 'Alexandrino' + ' ' + 'Passos')
# Da até para concatenar strings e fazer o casting de tipos de dados.
print('Lucas' + ' ' 'Passos' + ' ' 'tem' + ' ' + str(1.90) + ' ' 'de' + ' ' 'altura')

