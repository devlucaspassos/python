from traceback import print_exc


x = ('banana', 'morango', 'melão')

print(x) # --> Retornará:('banana', 'morango', 'melão')

y = enumerate(x)

print(list(y)) # --> Retornará: [(0, 'banana'), (1, 'morango'), (2, 'melão')]