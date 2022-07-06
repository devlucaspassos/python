# Aula 8 - Função input(): entrada de dados dos usuário.

# Veja abaixo a função input() que permite que o usuário ensira um dado.
nome = input('Qual seu nome? ')  # atribuindo o valor recebido a uma variável.
idade = int(input('Qual sua idade? '))  # É possível fazer o type casting de um dado da função print().
cidade = input('Qual cidade você nasceu? ')
ano_atual = 2022
ano_nasc = ano_atual - int(idade)  # Também é possível fazer o type casting na variável.

# Exibindo um texto utilizando as variáveis que receberam valores da função input().
print(f'O nome do usuário é {nome} e tem {idade} anos de idade.' f' {nome} nasceu no ano de {ano_nasc} na cidade de {cidade}.')



