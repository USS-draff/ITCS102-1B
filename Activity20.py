for a in range(1,11,1):
    for s in range(10, a, -1):
        print(' ', end=' ')
    for d in range(1, a, 1):
        print('*', end=' ')
    for f in range(1, a, 1):
        print('*', end=' ')
    print('*')
