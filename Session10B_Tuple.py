my_data = (10,20,30)
numbers = (
    (10,20,30),
    (40,50,60,70,80),
    (90,99)
)
#3D
large_data = (
    (
        ((10,20,30),
         (40,50,60,70,80),
         ),
        (
        (40,50,60,70,80),
        (90,99)
        )
    )
)
print("Tuple",my_data)
#indexing and Negative indexing
print("my_data[2]",my_data[2])
print("my_data[-2]",my_data[-2])
print("Tuple 2D: ",numbers)
print("numbers[2]",numbers[2])
print("numbers[1][4]",numbers[1][4])
print("numbers[-1][-2]",numbers[-1][-2])

print("Tuple 3D: ",large_data)
print("large_data[1]",large_data[1])
print("large_data[1][0][2]",large_data[1][0][2])
print("large_data[-2][-1][-5]",large_data[-2][-1][-5])

#Slicing
data = list(range(10,51,5))
print(data)
print("data[:5]",data[:5])
print(("data[6:]",data[6:]))
print("data[5:9]",data[5:9])
print("data[:-5]",data[:-5])
print("data[-5:-2]",data[-5:-2])

#Concatenation
data1 = (10,20,30)
data2 = (40,50,60)
data3 = data1+data2
print(data3)

#multiplication
data4 = data1*2
print(data4)

#membership Testing
print(10 in data1)
print(100 in data1)
print(10 not in data1)


student = {
    "name" : "Jimmy",
    "age":"20",
    "course": "BTech",
    "Interest":"Machine Learning"
}
#indexing and Negative Indexing
print(student)
print(student["name"])
print(student["age"])
#slicing
"""print(student[:"course"])
print(student["name":"Interest"])"""#Error


student2 = {
    "name" : "Jimmy"
}
#Concatenation#Error
"""student3 = student2+student
print(student3)"""
#Multiplication
"""print(student*2)""" #Error

#membership Testing
print("name" in student)
print("20" in student)#only for Key Values?
print("age" not in student2)
#Assignment
str1 = "Search the Candle rather than cursing the darkness"