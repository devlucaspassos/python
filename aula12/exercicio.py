# Exemplo de limitador de caracteres mínimos para criação de um login:

login_criado = input('Digite um login qe deseja utilizar: ')
qtd_caracteres = len(login_criado)
qtd_minima = 6

if qtd_caracteres < qtd_minima:
    print('Insira 6 ou mais caracteres')
else:
    print('Login criado com sucesso.')

# Algoritimo para saber a quantidade de caracteres de dois nomes inseridos por um usuário.
nome_1 = input('Digite um nome: ')
nome_2 = input('Digite um nome: ')

print(f'A soma do número de caracteres dos nomes {nome_1} e {nome_2} é: {len(nome_1) + len(nome_2)}')

