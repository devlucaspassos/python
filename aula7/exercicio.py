
# Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)

# Obter o IMC da pessoa com duas casas decimais

# Exibir um texto com todos os valores na tela usando o f-string.

nome = 'Otávio'
idade = 22
altura = 1.84
peso = 88
ano_atual = 2022

imc = peso / altura ** altura 

ano_nasc = ano_atual - idade  

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')