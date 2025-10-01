for i in range(1, 7, 1):
    for q in range(7, i, -1):
        print(' ', end=' ')
    for w in range(i, 0, -1):
        print(w, end=' ')
    for e in range(2, i + 1, 1):
        print(e, end=' ')
    print()