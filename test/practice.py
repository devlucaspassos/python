while True:
    nota_dig = input('Digite uma nota de 0 a 10: ')

    if nota_dig.isnumeric():
        if int(nota_dig) > 10 or int(nota_dig) < 1:
            print('Digite um valor de 1 a 10')
            continue
        else:
            print('Nota aplicada.')
            break
    else:
        print('Não foi possível inserir a nota, por favor digite um número.')
