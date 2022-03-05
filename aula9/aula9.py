# Palavras chaves IF, ELIF e ELSE e condições.

'''A Palavra chave if executa um estado se uma condição específica é verdadeira. Se a condição for falsa, outro estado pode ser executado (else). A palavra chave elif funciona como um "Se não", fazendo com que caso a condição anterior não seja verdadeira, os blocos de códigos dentro da palavra chave elif seja excutado.

As palavras-chave if else elif consistem em uma estrutura de controle. Elas nos possibilita, com base em uma determinada condição (True ou False), definir qual fluxo que a aplicação vai tomar. A condição é uma expressão que pode ser considerada tanto verdadeira (True) quando falsa (False), caso essa condição seja verdadeira, o trecho de código que está inserido abaixo da palavra-chave if será aplicado. Caso a condição seja falsa, o bloco de códigos de if será desconsiderado. 

A instrução else é colocada logo após o bloco de códigos de if ou elif, sendo ela opcional A palavra-chave else opera como um “Se não” para a condição estabelecida no if, ou seja, caso a condição não seja verdadeira, portanto falsa, o bloco de códigos dentro das chaves de if será desconsiderado, sendo executado em seu lugar, o bloco de códigos contido em else.

Já palavra-chave elif é uma maneira em Python de dizer "Se as condições anteriores não forem verdadeiras, tente esta condição.

É possível inserir quantas linhas de códigos você quiser em cada bloco, contanto que você siga a
hierarquia

'''
if False:
#HIERARQUIA: O bloco de códigos deve ter 4 espaços em relação a a palavra-chave
    print('Verdadeiro')
elif True:  
    '''
    Caso a condição if acima não for verdadeira, o bloco de codigo abaixo será executado.
    Quando o interpretador encontra uma condição verdadeira (True)
    '''
    print('Isso é verdadeiro') 

    nome = input('Como você se chama? ')

    print(f'Meu nome é {nome}')
elif False:  #->Essa linha só sera executada se as condições anteriores não forem verdadeiras (False)
    print('Isso também é verdadeiro')

    num_1 = input('Digite um número ')
    num_2 = input('Digite outro número ')
    mult_num = int(num_1) * int(num_2)

    print(f'O resultado da multiplicação é: {mult_num}')

else:
    ''' O bloco de códigos presente abaixo só será executado caso todas as condições acima não forem verdadeiras. Caso nenhuma das condições seja verdadeira, nenhuma linha de código seja executada.'''
    print('Não é verdadeiro')