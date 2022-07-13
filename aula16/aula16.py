# Aula 16 - Laço de repetição while

# 1 - Laço while

while 10 == 9:  # --> Condição
    print('banana')
    print('morango')
    print('uva')

print('Não será executada')  
# A função print() acima só será executada quando o laço while foi cessado.


# 2 - Contador e acumulador


contador = 1  # O contador é acumulado de forma linear, ex: 0, 1, 2, 3...

while contador <= 100:
    print(contador)
    contador += 1

contador = 1 
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador += contador  # Novo valor atribído a variável 'acumulador'.
    contador += 1  # Novo valor atribído a variável 'contador'.


# 3 - Palavra-chave continue

x = 0

while x <= 10:
    if x == 3:
        x += 1
        continue  # A iteração terá fim e uma nova verificação da expressão será feita
    print(x)
    x += 1
print('Fim!')


# 4 - Palavra-chave break


x = 0 

while x < 10:
    if x == 3:
        break  # A repetição terá um fim definitivo.
    print(x)
    x = x + 1

print('Fim!')


# 5 - Laço while e estrutura condicional else

contador = 1 
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
else: 
    print('Aplicação do comando condicional else.')


# 6 - Iterando string com while

#        Índices
#        0123456789.......................34 
frase = "O rato roeu a roupa do rei de Roma"
tamanho_frase = len(frase)  # Essa string tem 34 caracteres.
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1


#        Índices
#        0123456789.......................34
frase = "O rato roeu a roupa do rei de Roma"
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
