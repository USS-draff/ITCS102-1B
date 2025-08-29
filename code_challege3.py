name = input("What is your name ? --->")
fare = eval(input("fare fee ---> "))
isStudent = input("Are you currently a student (yes/no) ")

if isStudent == 'yes':
	discount = fare *0.2
	#fare -= discount
	new_fare = fare - discount
	print("Hi ",name)
	print("Your Discount is ",discount)
	print("Your new fare is ",new_fare)
else:
	print("Sorry ",name, "You are not eligible for student discount")
