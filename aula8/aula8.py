#Input: entrada de dados dos usuário.


input('Qual o seu nome? ')  # ---> Função string() que permite que o usuário ensira um dado (string)
#O dado inserído pelo usuário será sempre retornado como uma str.

'''é possível atribuir essa função input em uma variável. Nesse caso, o dado inserido pelo usuário
será atribuído a aquela variável.
'''
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))  #--> Dá para fazer o type casting de um dado da função print
cidade = input('Qual idade você reside? ')
ano_atual = 2022
ano_nasc = ano_atual - int(idade)  # ---> Também é possível fazer o type casting no nome da variável

print()
print(f'O nome do usuário é {nome} e tem {idade} anos de idade.' f' {nome} nasceu no ano de {ano_nasc} na cidade de {cidade}.')
'''A função print acima exibirá: "O nome do usuário é Lucas e tem 24 anos de idade. Lucas nasceu no ano de 1998 na cidade de Acaraú."'''



