print("ODD number summation")

s = 0
for number in range (0, 10, 1):
    h = eval(input("Enter the number ---> "))
    if h % 2:
        s += h
print("The Summation of all ODD number ",s)
