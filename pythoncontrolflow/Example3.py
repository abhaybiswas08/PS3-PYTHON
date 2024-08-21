print("Enter the Current Temperature: ")
temperature_input = float(input())

if (temperature_input > 500.0):
	print("HW")
elif (temperature_input > 100.0):
	print("BP")
else:
	print("None")
