
data = list(range(10,101,10))
print("data:",data)

for idx in range(len(data)):
    print(data[idx])

for element in data:
    print(element) ##Can be used to print elements in a set

student = {
    "rollno":101,
    'name': 'fionna',
    "age": 18

}
items = student.items()
for item in items:
    print(item)
    print(item[0])

keys = student.keys()
for key in keys:
    print(key)

for key in keys:
    print(key,student[key])

