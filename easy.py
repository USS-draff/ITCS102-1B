for q in range(1, 8, 1):
    for w in range(7 ,q , -1):
        print(' ', end=' ')
    for e in range(1, q*2, 1):
        print('*', end=' ')
    print()

for a in range(1, 7, 1):
    for s in range(1, a+1, 1):
        print(a, end=' ')
    print()