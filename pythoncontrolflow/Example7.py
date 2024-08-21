day_count = int(input()) % 8  # 100 % 8

match (day_count):
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")
	case 7:
		print("Sunday")
	case _:							# Default
		print("Not A Valid Week Day....")
