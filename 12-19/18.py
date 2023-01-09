userNumber = int(input("Please enter a Number? "))
if userNumber < 10:
	print("Too Low")
elif userNumber >= 10 and userNumber <= 20:
	print("Correct")
else:
	print("Too High")