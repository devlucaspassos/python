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
