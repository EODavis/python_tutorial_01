dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict1['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict3 = {
    'value': 33
}

dict2 = dict3

print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict3 =", dict3)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict3 points to:", id(dict3))
