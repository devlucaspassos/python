nome = input('Escreva seu nome aqui: ')

if nome.isdigit():
    print('Números não são aceitos, digite seu nome.')
else:
    nome = len(nome)
    if nome <= 4: 
        print('Seu nome é muito curto, digite novamente.')
    elif nome >= 10:
        print('Seu nome é muito longo, digite novamente.')
    else:
        print('Nome aceito.')
