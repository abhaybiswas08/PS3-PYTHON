def foo1():
	print("Function Foo-1 Is Called...")
	print("***")


def foo2():
	print("Function Foo-2...")
	foo1()


print("Python Program Is Running...")
foo2()
print("End")
