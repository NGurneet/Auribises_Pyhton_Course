"""Explore Multivalued Container"""
numbers = list(range(10,101,10))
print("numbers:",numbers)
print("numbers Type:",type(numbers))
numbers.append(110)
numbers.append(115)
print("numbers:",numbers)
print("Sum is:",sum(numbers))
print("Min is:",min(numbers))
print("Max is:",max(numbers))
print("Length is:",len(numbers))
reverse_number = list(reversed(numbers))
print("reverse_number",reverse_number)

print("INdex: ",reverse_number.index(50))
numbers.append(20)
print("How Many times no comes:  ",numbers.count(20) )

data = [70,30,50,90,20]
print("Data:",data)
print("Sorted Data:" ,sorted(data))

names = ["john","anna","sia","angel","Jimmy","kim"]
print("Sorted Names:",sorted(names))
print(min(names))
print(max(names))
"""data.remove(30)
names.remove("anna")
print(names)
print(data)

del names[2]
print(names)
data.pop()
print(data)
data.pop(0)
print(data)"""

"""data.clear()
print(data)"""

data.insert(2,77)
print(data)
data.insert(-1,111)
print(len(data))
data.insert(7,79)
print(data)
