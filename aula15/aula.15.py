# Aula 15 - Índices em Python e fatiamento de índices.

# Postivos        [012345678]
texto          =  'Python S2'
# Índices negativos     -[987654321] --> -9, -8, -7, etc.
texto                  = 'Python S2'

print(texto[3])  # >> h
# Na função print acima, foi resgatado o índice 3 da variável texto, que é a letra 'h'.

print(texto[-1])  # >> 2
# Índice negativo do valor "2" dentro da string.

# caso seja feita um acesso de um índice inexistente, ocorrerá um erro.
print(texto[9])  # >> IndexError: string index out of range

# Fatiamento de índices

texto = 'Python S2'

nova_string = texto[2:6] 
# No exemplo acima, foi atribuído a variável nova_string os valores "thon".
print(nova_string)  # >> Será exibido o valor 'thon', que são os índices 2:6 da variável texto.

# Caso deseje acessar o índices do início ou fim da string, é possível deixar um dos valores vazios.

nova_string = texto[:6]  # Aqui o valor vazio significa o primeiro índice.
print(nova_string)  # >> Python

nova_string = texto[7:] # Aqui o valor vazio significa o último índice.
print(nova_string)  # >> S2

# Fatiamento com intervalos

texto = 'Python S2'
nova_string = texto[0::2]
print(nova_string)  # >> Pto 2