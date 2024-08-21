class Person:
	# Private Variables
	__name: str = None
	__age: int = None

	# Private Function
	def __init__(self, lc_name: str, lc_age: int):
		self.__name = lc_name
		self.__age = lc_age

	def set_name(self, lc_name: str):
		if type(lc_name) is str:
			self.__name = lc_name

	def set_age(self, lc_age: int):
		if type(lc_age) is int:
			self.__age = lc_age

	def get_name(self) -> str:
		return self.__name

	def get_age(self):
		return self.__age

	def __str__(self):
		return f"{self.__name}..... {self.__age}\n"

	@classmethod
	def describe(self):
		print("Person Class Describe Method")


Person.describe()
my_obj: Person = Person(lc_name = "Abhay", lc_age = 20)
print(my_obj)
