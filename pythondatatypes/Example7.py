my_data = dict()
print(my_data)

my_data["Key"] = "Value"
print(my_data)

my_data["Name"] = "Abhay"
my_data["Age"] = 21

print(my_data)
print(my_data.get("Name-1"))

my_data.pop("Name")
print(my_data)

my_data = {
        'a': 10,
        'b': 20,
        'c': 30,
        'd': 50,
        21: 2003
}
print(my_data)

my_data.pop('d')
print(my_data)

my_data.popitem()
print(my_data)

for k, v in my_data.items():
    print(k, v, sep=":")

print(my_data.values())

for item in my_data.items():
    print(item)

for keys in my_data.keys():
    print(my_data[keys])
