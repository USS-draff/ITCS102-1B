sub = eval(input("Enter the number of coluoms----->"))

for q in range(1, 11, 1):
    for w in range(1 ,sub+1 ,1):
        print(f"{q} x {w} = {q * w}", end='\t')
    print()