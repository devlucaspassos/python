#        Índices
#        0123456789.......................34
frase = "O rato roeu a roupa do rei de Roma"
tamanho_frase = len(frase)
contador = 0
nova_string = ''


#print(tamanho_frase)  # --> Será exibido o valor "34".

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1

print(nova_string)