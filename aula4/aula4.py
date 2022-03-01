'''
TIPOS DE DADOS

str ---> string ---> 'texto' ou "texto" ---> print('texto')
int ---> inteiro ---> 12 ou -12 ---> print(123) --->São números inteiros tanto positivo quando negativo, incluindo 0. 
float ---> real/ponto flutuante ---> 12.64 ou -89.92 ---> print(10.52) ---> São números fracionários, tanto positivo quando negativo.
bool ---> booleano/lógico ---> True ou False 
'''
'''
print('Lucas', type('Lucas'))
print(10, type(10))
print(-50.52, type(-50.52))
# print(10 <= 15, type(10 <= 15))
print('L' == 'l', type('L' == 'l')) '''

 
#print('Lucas', type('Lucas'), bool('Lucas')) # ---> saída: true
"""---> Quando uma string estiver vazia, ou os valores dos dados forem 0, 0.0 ou também estiverem vazios, o valor booleano desse dado é false. Do contrário, caso a string contenha valores, ou os valores dos dados de int e float forem números diferentes de 0 ou 0.0, o valor booleano desse dado é true"""

'''
#exemplo 1
print('10')  # ---> O valor 10, por estar entre aspas é interpretado como string (str)
print(int('10'))  # ---> após por o valor '10' dentro da função int, ele é convertido para um dado do tipo int.

#exemplo 2

print(10.50)  # ---> O valor 10.50, por ter casas decimais, é um dado do tipo float. 
print(int(10.50))  # ---> Após o uso da função int, o valor 10.50 foi convertido para um dado do tipo int.
'''



# String: Nome
print('Lucas', type('Lucas'))
# Idade: int
print(23, type(23))
# Altura: float
print(1.90, type(1.90))
# É maior que 18 anos
print(23 > 18, type(23 > 18))






