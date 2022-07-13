
# Aula 5 - Operadores aritméticos: +, -, *, **, /, //, %, ().

print(10 + 10)  # Operador de soma.
print(10 - 10)  # Operador de subtração.
print(10 * 10)  # Operador de multiplicação.
print(10 ** 10)  # Operador de potenciação (Nesse caso vai ser 10 elevado a 10 = 100).
print(10 / 10)  # Operador de divisão.
print(10 // 10)  # Operador de divisão inteira (vai arredondar os números).
print(19 % 18)  # Operador módulo (exibe o resto de uma divisão).
print(10 + (20 - 10) * (25 - 15)) # Alteração de precendência com os parênteses.

# O operador de multiplicação também pode multiplicar strings, criando uma repetição, veja o exemplo abaixo.
print(10 * 'A')  # >> AAAAAAAAAA
 
# O operador de soma (+) quando usado entre strings, faz a concatenação (Junção) das mesmas.
print('abaca' + 'xi')  # >> acabaxi

# Concatenando mais várias strings.
print('gosto' + ' ' + 'de' + ' ' + 'café')  # >> gosto de café

# É possível concatenar strings e fazer o casting (conversão) de tipos de dados.
print('João' + ' ' 'tem' + ' ' + str(19) + ' ' + 'anos' + ' ' 'de' + ' ' 'idade')
# >> João tem 19 anos de idade

