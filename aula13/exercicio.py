# Crie um algoritmo que peça pra o usuário criar um login. Caso o login digitado pelo usuário contenha 5 ou menos caracteres, a mensagem "Mínimo de 5 caracteres" deverá exibida. Caso o login digitado pelo usuário contenha 12 ou mais caracteres, a mensagem 'Máximo de 12 caracteres" deverá ser exibida.

nome = input('Crie um login: ')
if nome.isdigit():
    print('Números não são aceitos.')
elif len(nome) <= 5:
    print('Mínimo de 5 caracteres.')
elif len(nome) >= 12:
    print('Máximo de 12 caracteres')
else:
    print('Login criado com sucesso.')


# Crie um algoritmo que pergunte o horário ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada, exemplo: "Bom dia!" caso o horário digitado seja das 0h - 11h, "Boa tarde" caso o horário seja das 12h - 17h e "Boa noite" caso o horário seja das 18h - 23h.

horario = input('Digite um horário: ')

if horario.isnumeric():
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa Tarde')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
else:
    print('Digite apenas o horário (00-23).')
    

# Crie um algoritmo que peça para o usuário digitar um número inteiro, e informe se este número é um número par ou um número ímpar. Caso o usuário não digite um número inteiro, informe que o número digitado pelo o usuário não é um número inteiro.

numero = (input('Digite um número inteiro: '))

if numero.isdecimal():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
else:
    print('Digite apenas números.')