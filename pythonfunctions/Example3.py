def fib(n) -> None:
	a = 0
	b = 1
	c = None

	while a < n:
		print(a, end = '  ')
		c = a + b
		a = b
		b = c
	print()


fib(56)
