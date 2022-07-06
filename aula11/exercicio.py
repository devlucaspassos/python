# Exemplo de um verificador de login e senha.

login = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

usuario_bd = 'maria123'
senha_bd = 'maria321'

if login == usuario_bd and senha == senha_bd:
    print('Login realizado com sucesso.')
else:
    print('Não foi possível realizar o login.')

# João é um agricultor que produz diversos tipos de frutas em sua propriedade, um mercado local quer comprar determinados tipos de frutas que João produz, porém, o mercado impõe duas condições para a compra. O mercado só deverá comprar as frutas de João caso as mesmas atendam a um padrão de qualidade ou caso as frutas estejam com um preço abaixo do mercado.

# frutas de João

qualidade_boa = False
preco_bom = True

if qualidade_boa == True or preco_bom == True:
    print('O mercado comprou as frutas de João.')
else:
    print('O mercado não comprou nenhuma fruta de João')

# Crie um algoritmo que calcule o reajuste de salário em uma empresa. O reajuste varia de acordo com o salário dos funcionáis, veja abaixo a tabela de reajuste.

# Salários
# R$1100,00 a R$ 2000,00 - Reajuste de 10% 0,
# R$2100,00 a R$ 3000,00 - Reajuste de 8% 
# R$3100,00 ou maior - Reajuste de 5% 

while True:
    salario = int(input('Digite o salário que será reajustado: '))


    if salario >= 1100 and salario <= 2099:
        salario = salario + salario * 0.10
        print(f'O valor do salário reajustado é:{salario}.')
    elif salario >= 2100 and salario <= 3099:
        salario = salario + salario * 0.08
        print(f'O valor do salário reajustado é:{salario}.')
    elif salario >= 3100:
        salario += salario * 0.05
        print(f'O valor do salário reajustado é:{salario}.')