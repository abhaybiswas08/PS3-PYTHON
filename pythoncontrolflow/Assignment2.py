error_d = int(input())

match (error_d):
	case 100:
		print("Information Status Code")
	case 200:
		print("Query Executed")
	case 300:
		print("Redirecting Route")
	case 400:
		print("Client Route")
	case 500:
		print("Internal Server Error")
	case _:							# Default
		print("Unknown Code...")
