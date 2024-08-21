import os

current_address = os.getcwd()
print("Complete Path = " + current_address)

os.chdir("C:/Users/ACER/Desktop/Practice School - 3/PS-3/PS3")
print(os.getcwd())
print(os.listdir())
