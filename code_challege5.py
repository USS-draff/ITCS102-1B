number = eval(input("Enter the number ---->   "))
factorial = 1
for y in range (number, 0, -1):
    factorial *= y
print("The factorail number of",number,"is",factorial)