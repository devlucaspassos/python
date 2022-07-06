# Exemplo de uso de operadores relacionais em um verificador de idade.

nome = input('Digite seu nome ') 
idade = int(input('Digite sua idade '))
# Limite de idade para pegar o empréstimo.
idade_minima = 20
idade_maxima = 30

if idade >= idade_minima and idade <= idade_maxima:
    print(f'Parabéns sr.{nome}, seu crédito foi aprovado.')
else:
    print('Que pena, você não tem os requisitos para crédito.')