# Aula 13 - Métodos isdecimal(), isdigit() e isnumeric().


num_1 = input('Digite um número: ')


print(num_1.isnumeric())  # >> Retornará True se o valor de num_1 for um valor numérico (0-9).

print(num_1.isdecimal())  # >> Retornará True se o valor de num_1 for um valor decimal (0-9).

print(num_1.isdigit())  # >> Retornará True se o valor de num_1 for um digito (0-9).