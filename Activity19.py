for q in range(1, 11, 1):
    for w in range(1, q, 1):
        print('@', end=' ')
    for e in range(10, q, -1):
        print('&', end=' ')
    print()