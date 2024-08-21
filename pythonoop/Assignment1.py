# DocString Comment
class Teacher:
	"""
	@:param First Name
	@:param Last Name
	@: param Last Qualification
	@: param Age
	"""
	__first_name__: str = None
	__last_name__: str = None
	__last_qualification__: str = None
	__age__: int = None

	# Getter Methods/Functions
	def get_first_name(self):
		"""
		Getter Method which returns the First Name
		:return: str
		"""
		return self.__first_name__

	def get_last_name(self):
		"""
		Getter Method which returns the Last Name
		:return: str
		"""
		return self.__last_name__

	def get_last_qualification(self):
		"""
		Getter Method which returns the Last Qualification
		:return: str
		"""
		return self.__last_qualification__

	def get_age(self):
		"""
		Getter Method which returns the Age
		:return: str
		"""
		return self.__age__

	# Setter Methods/Functions
	def set_first_name(self, lcFirstname):
		self.__first_name__ = lcFirstname

	def set_last_name(self, lcLastName):
		self.__last_name__ = lcLastName

	def set_last_qualification(self, lcLastQualification):
		self.__last_qualification__ = lcLastQualification

	def set_age(self, lcAge):
		self.__age__ = lcAge

	def __str__(self):
		return f"{self.__first_name__}.... {self.__last_name__}.... {self.__last_qualification__}.... {self.__age__}...."


obj = Teacher()
obj.set_first_name("Harshad")
obj.set_last_name("Mehta")
obj.set_last_qualification("B. Com")
obj.set_age("47")

print(obj)
