# DocString Comment
class Car:
	"""
	@:param BrandName
	@:param EngineType
	@: param Color
	@: param Mileage
	"""
	__brand_name__: str = None
	__engine_type__: str = None
	__color__: str = None
	__mileage__: float = None

	# Getter Methods/Functions
	def get_brand_name(self):
		"""
		Getter Method which returns the Brand Name
		:return: str
		"""
		return self.__brand_name__

	def get_engine_type(self):
		"""
		Getter Method which returns the Engine Type
		:return: str
		"""
		return self.__engine_type__

	def get_color(self):
		"""
		Getter Method which returns the Color
		:return: str
		"""
		return self.__color__

	def get_mileage(self):
		"""
		Getter Method which returns the Color
		:return: str
		"""
		return self.__mileage__

	# Setter Methods/Functions
	def set_brand_name(self, lcBrandname):
		self.__brand_name__ = lcBrandname

	def set_engine_type(self, lcEngineType):
		self.__engine_type__ = lcEngineType

	def set_color(self, lcColor):
		self.__color__ = lcColor

	def set_mileage(self, lcMileage):
		self.__mileage__ = lcMileage

	def __str__(self):
		return f"{self.__brand_name__}.... {self.__engine_type__}.... {self.__color__}.... {self.__mileage__}...."


obj = Car()
obj.set_brand_name("BMW")
obj.set_engine_type("Twin-Turbo 4.4 Liter V-8")
obj.set_color("Black")
obj.set_mileage("9.1")

print(obj)
