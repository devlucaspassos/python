# Aula 2 - Função print() e seus parâmetros sep e end.

print('Olá, mundo!')  # >> Olá, mundo
print(123456)  # >> 123456

# Os parâmetros podem ser separados por vírgula, e serão exibidos na tela com espaços entre sí.
print('banana', 'morango', 'cajú')  # >> banana morango cajú

# Utilizando o parâmetro sep, você pode substituir o espaço padrão entre as strings por outro caractere, como o * por exemplo.
print('cachorro', 'avestruz', sep='*')  # >> cachorro*avestruz

# Utilizando o parâmetro end, você pode substituir o caractere final da string, que por padrão é a quebra de linha, por outro caractere.

print('eu', 'quero', end=' ')  # Espaço como valor deste parâmetro.
print('comer', 'pizza') 
# >> eu quero comer pizza