'''
Iniciar com letras, pode conter números, separar _, letras minúsculas.
'''
# Exemplo de variáveis abaixo
nome = 'Lucas'  # --> Exemplo de string sendo atribuída a variável "Lucas"
idade = 23  # --> Exemplo de int sendo atribuída a variável "idade"
altura = 1.90  # --> Exemplo de float sendo atribuida a variável altura
i_maior = idade > 18  # --> Exemplo de comparação utilizando a variável "idade"
mes_1 = True  # --> Variável com número no nome e valor bool
data_atual = 2022  # --> Váriavel com _ separando as duas palavras

# Uso das variáveis

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maior que 18 anos?', i_maior)

# As funções prints acima irão exibir os seguintes valores:
'''Nome: Lucas
Idade: 23
Altura: 1.9
Maior que 18 anos? True'''

#Também é possível utilizar as variáveis para fazer operações
print(idade * altura) # ---> a var idade está associada ao int 23 e a var altura ao float "1.90".
#A função print acima irá exibir "43.699999999999996" (1.90 * 23 = 43.699999999999996)