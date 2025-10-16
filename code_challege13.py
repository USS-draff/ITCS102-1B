enter0 = input("Enter you name sir/ma'am ---->")
print("***************************\nODD NUMBER SUMMATION, press 0 to stop.\n***************************")
sum = True
sun = 0
dun = ''

while sum:
    enter = eval(input("Enter the a ramdom number----->"))
    if enter %2 == 1:
        print("ODD Number ditected")
        sum += sun
        dun += str(enter) + " "
        continue
    elif enter == 0:
        print("number 0 ditected ,LOOP TERMINATED")
        break
    else:
        if enter %2 == 0:
            print("EVEN number ditected")
        else:
            print("Loop stop.")
            continue
print(f"Hi {enter0}, your total of number input is {sun}")
print(f"Here's all number of number you input in the loop {dun}")
