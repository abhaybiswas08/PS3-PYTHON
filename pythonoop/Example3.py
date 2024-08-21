# DocString Comment
class My_TV:
	"""
	@:param BrandName
	@:param ModelName
	@: param BandWidth
	"""
	__brand_name__: str = None
	__model_number__: str = None
	__band_width__: str = None

	def __init__(self):
		print("Constructor Called...")

	# Getter Methods/Functions
	def get_brand_name(self):
		"""
		Getter Method which returns the Brand Name
		:return: str
		"""
		return self.__brand_name__

	def get_model_number(self):
		"""
		Getter Method which returns the Model Number
		:return: str
		"""
		return self.__model_number__

	def get_band_width(self):
		"""
		Getter Method which returns the BandWidth
		:return: str
		"""
		return self.__band_width__

	# Setter Methods/Functions
	def set_brand_name(self, lcBrandname):
		self.__brand_name__ = lcBrandname

	def set_model_number(self, lcModelnumber):
		self.__model_number__ = lcModelnumber

	def set_band_width(self, lcBandwidth):
		self.__band_width__ = lcBandwidth

	def __str__(self):
		return f"{self.__brand_name__}.... {self.__model_number__}.... {self.__band_width__}...."


obj = My_TV()
obj.set_brand_name("OnePlus")
obj.set_model_number("55Q1IN-1")
obj.set_band_width("8MHz")

print(obj)
