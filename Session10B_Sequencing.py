my_data = [10,20,30]

numbers = [
    [10,20,30],
    [40,50,60,70,80],
    [90,99,105]
]
#indexing
print(len(my_data))
print(my_data[1])

print(len(numbers))
print(numbers[1])
print(numbers[1][2])
print(numbers[-1][2])

#3D List
large_data = [
    [
        [10,20,30],
        [40,50,60,70,80],
        [90,99]

    ],
    [
        [10,20,30],
        [40,50,60,70,80],
        [90,99],

    ]
]
#Negative Indexing
print("3d",large_data[-2][-1][-2])
#slicing
data = list(range(10,101,10))
print("data",data)
print("data[:5]",data[:5])
print(("data[6:]",data[6:]))
print("data[5:9]",data[5:9])
print("data[:-5]",data[:-5])
print("data[-5:-2]",data[-5:-2])

#concatenation
data1 = [10,20,30]
data2 = [40,50,60]
data3 = data1+data2
print(data3)

#multiplicity
data4 = data1*2
print(data4)

#membership Testing
print(10 in data1)
print(100 in data1)
print(10 not in data1)


