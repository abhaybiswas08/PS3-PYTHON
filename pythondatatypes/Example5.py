"""
Tuple Data Types In Python
"""

immutable_list = tuple(["Obj_1", "Obj_2", "Obj_1", 1212])

print(immutable_list)
print(immutable_list.count("Obj_1"))
print(immutable_list.index(1212))


s_list = tuple(["X"])
print(s_list)

c_list = list(s_list)
print(c_list)

c_list.append("Y")
c_list.append("Z")
print(c_list)

t_list = tuple(c_list)
print(t_list)
