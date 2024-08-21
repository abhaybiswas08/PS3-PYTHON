m = int(input("Enter Value of M: "))
n = int(input("Enter Value of N: "))

while (m != n):
	if (m > n):
		m = m - n
	else:
		n = n - m

print(f"GCD: {m}")
