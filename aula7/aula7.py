# Aula 7 - Formatando texto com f-string.

nome = 'Maria'
peso = 58
altura = 1.60
idade = 21
imc = peso / (altura * altura)

# Veja abaixo a exibição de um texto sem a utilização do f-string.
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
# >> Maria tem 21 anos de idade e seu IMC é 22.656249999999996

# Veja abaixo abaixo a exibição de um texto onde foi aplicado o f-string.
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}') 
# >> Maria tem 21 anos de idade e seu IMC é 22.66

# Você pode inserir variáveis dentro da f-string, contanto que as delimite com chaves {}.
