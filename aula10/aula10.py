'''
OPERADORES RELACIONAIS/COMPARAÇÃO == > >= < <= !=

Operadores de comparação

Também conhecidos como operadores relacionais.

servem para formar as expressões condicionais para o comando `if`.

Operadores:

Igual (==) - Verifica se os valores comparados são iguais.
Diferente (!=) - Verifica se os valores comparados são diferentes.
Menor (<) - Verifica se o valor da esquerda é menor que o valor da direita.
Maior (>) - Verifica se o valor da esquerda é maior que o valor da esquerda)
Menor igual (<=) - Verifica se o valor da esquerda é menor ou igual ao valor da direita.
Maior igual (>=) - Verifica se o valor da esquerda é maior ou igual ao valor da esquerda.
'''

#Exemplo usando variáveis do tipo int
num_1 = 2 #int
num_2 = 2 #int

nome_1 = 'Lucas'
nome_2 = 'Passos'

print(num_1 == num_2)  # Essa expressão é verdadeira (True), porque 2 é igual a 2.

#Exemplo de uso com variáveis do tipo str
print(nome_1 == nome_2)  
# Essa expressão é falsa, pois os valores atribuídos as variáveis são diferentes.

#Outro exemplo de uso dos operadores relacionais/comparação

nome = input('Digite seu nome ') 
idade = input('Digite sua idade ')
# Limite de idade para pegar o emprestimo.
idade_minima = 20 # Muito jovem
idade_maxima = 30 # Véi demais



if int(idade) <= idade_minima:
    print(f'{nome} não pode pegar o empréstimo com o agiota.')
elif int(idade) >= idade_maxima: 
    print(f'{nome} não pode pegar o empréstimo com o agiota.')
else: 
    print(f'{nome} pode pegar empréstimo com o agiota.')