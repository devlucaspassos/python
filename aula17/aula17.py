# Aula 17 - laço for in e iteração de string com for.

# Exemplo de exibição da palavra Python utilizando ambos os laços while e for.

texto = 'Python'

c = 0 

while c < len(texto):
    print(texto[c])
    c += 1

for n in texto:
    print(n)

# Exemplo de verificação de nomes que começam com a letra "J".

nomes = ['João', 'Maria', 'Betinho']

for valor in nomes:
    if valor.lower().startswith('j'):
        print('há um ou mais nomes que começam com a letra "J".')
        break
else:
    print('Não há nomes que começam com a letra "J".') 