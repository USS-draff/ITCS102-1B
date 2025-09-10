temp = eval(input("What is the temperature right now --->"))

if temp <= 0:
	print("temp is considered extremly cold")
elif temp >= 1 and temp <= 15:
	print("temp is considered extremly cold")
elif temp >= 16 and temp <= 30:
	print("Cold Temperature")
elif temp >= 31 and temp <= 38:
	print("Lukewarm Temperature")
elif temp >= 39 and temp <= 42:
	print("Warm Temperature")
elif temp >= 43 and temp <= 50:
	print("Hot Temperature")
elif temp >= 51 and temp <= 60:
	print("Extremely Hot Temperature")
elif temp >= 61:
	print("Burning Temperature")
else:
	print("Invalid Temperature")

