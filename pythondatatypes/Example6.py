s_set = set()  # OR s_set = {}
print(s_set)

s_set = {"Apple", "Cherry", "Orange", "Apple"}
print(s_set)

print("Orange" in s_set)
print("Banana" in s_set)

s_set.remove("Cherry")
print(s_set)

s_list = [12, 14, 54, 32, 77, 41, 12, 65, 14, 54, 77, 12, 65, 41]
print(s_list)

s_set_1 = set(s_list)
print(s_set_1)

s_tuple = ("Eat", "Sleep", "Play", "Ride", "Sleep", "Play", "Eat", "Ride")
print(s_tuple)

s_set_2 = set(s_tuple)
print(s_set_2)

set_s = set("abcdefgh")
print(set_s)

set_a = set("abc")
set_b = set("cde")

set_c = set_a.intersection(set_b)
print(set_c)

set_d = set_a.union(set_b)
print(set_d)

set_d.update("f")
print(set_d)
