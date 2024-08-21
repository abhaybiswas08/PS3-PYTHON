# WAP To Get Fibonacci Numbers using Loop

def fib(n):
	fib_series = [0, 1]

	for i in range(2, n):
		fib_series.append(fib_series[-1] + fib_series[-2])
	return fib_series


print(fib(12))
