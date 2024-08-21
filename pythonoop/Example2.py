class ThumbDrive:
	brand_name: str = None
	memory_size: int = None
	data: list = []  	# In-Memory (Caching)

	def read_data(self, byte):
		index = self.data.index(byte)
		if index is index >= 0:
			return self.data[index]
		return None

	def write_data(self, byte):
		self.data.append(byte)

	def get_size(self):
		return len(self.data)

	def __str__(self):
		return f"{self.brand_name}.... {self.memory_size}.... {self.data}...."


if __name__ == "__main__":
	obj = ThumbDrive()
	obj.brand_name = "SanDisk"
	obj.memory_size = 1024 * 64
	obj.write_data("My_File.txt")
	obj.write_data(121212)
	print(obj.read_data("My_File.txt"))

	print(obj)
