nome = input('Digite seu nome: ')
horario = input('Digite o horário(00h-23h):')


if horario.isdigit():
    horario = int(horario)
    if horario <= 11:
        print(f'Bom dia {nome}')
    elif horario >= 12 and horario <= 17:
        print(f'Boa tarde {nome}')
    elif horario >=18 and horario <=23:
        print(f'Boa noite {nome}')
    elif horario > 23:
        print('Digite um horário de 00h as 23h')
else:
    print('Digite um número de 0 a 23.')