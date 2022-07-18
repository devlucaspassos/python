# Aula 18 - função range()

# Criando sequências

x = range(10) 

for n in x:
    print(n)  # >> Vai exibir cada número da sequência.

y = range(0, 101, 10)

for n in y:
    print(n)  # >> Vai exibir cada número da sequência.

# Multiplos de 8.

mult_3 = range(0, 100, 8)

for n in mult_3:
    print(n)

# Times

times = ['Fla', 'Cor', 'Pal', 'Vas', 'Bot'] 

for time_1 in times:
    for time_2 in times:
        if time_1 != time_2:
            print(f'{time_1} vs {time_2}')