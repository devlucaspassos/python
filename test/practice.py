x = range(8)

c1 = 0
c2 = 10

for n in x:
    if c1 == 0 or c2 == 10:
        print(c1, c2)
    c1 += 1
    c2 -= 1 
    print(c1, c2)