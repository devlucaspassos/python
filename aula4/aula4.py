# Aula 5 - Type casting - Conversão de dados

# O valor 10, por estar inserido entre aspas é interpretado como string (str).
print('10')  # >> 10 (string)

# A função int() vai converter o dado do tipo string (str) para o tipo inteiro (int).
print(int('10'))  # >> 10 (inteiro)

# O valor 10.50, por ter casas decimais, é um dado do tipo float. 
print(10.50)  # >> 10.50 (float)

# A função str() vai converter o tipo de dado float em um tipo de dado string (str).
print(str(10.50))  # >> 10.50 (str)

x = 'banana' 
y = ''  # string vazia

print(x)  # >> banana (str)
print(bool(x))  # >> True 
print(bool(y))  # >> False




# Após o uso da função bool, o dado 'Lucas' que é do tipo str foi convertido para bool.
# Note que, a saída foi true, pois como foi dito cima, string com valores são dadas como true.