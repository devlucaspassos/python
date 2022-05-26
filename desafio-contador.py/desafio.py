# --> EXERCÍCIO DE CONTADORES - PYTHON
# --> laço de repetição while
c1 = 0
c2 = 10

while c1 < 8 and c2 > 2:
    if c1 == 0 or c2 == 10:
        print(c1, c2)
    c1 += 1
    c2 -= 1
    print(c1, c2)

# --> laço de repetição for

x = range(8)

c1 = 0
c2 = 10

for n in x:
    if c1 == 0 or c2 == 10:
        print(c1, c2)
    c1 += 1
    c2 -= 1 
    print(c1, c2)