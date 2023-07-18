my_data = {10,20,30}
numbers = {
    {10,20,30},
    {40,50,60,70,80},
    {90,99}
}
#3D
large_data = {
    {
        {{10,20,30},
         {40,50,60,70,80},
         },
        {
            {40,50,60,70,80},
            {90,99}
        }
        }
}
print("Set",my_data)
#indexing and Negative indexing
"""print("my_data[2]",my_data[2])
print("my_data[-2]",my_data[-2])
print("Tuple 2D: ",numbers)
print("numbers[2]",numbers[2])
print("numbers[1][4]",numbers[1][4])
print("numbers[-1][-2]",numbers[-1][-2])

print("Tuple 3D: ",large_data)
print("large_data[1]",large_data[1])
print("large_data[1][0][2]",large_data[1][0][2])
print("large_data[-2][-1][-5]",large_data[-2][-1][-5])
"""#Error
#Slicing
data = list(range(10,51,5))
print(data)
print("my_data[:5]",my_data[:5])
print(("my_data[6:]",my_data[6:]))
print("my_data[5:9]",my_data[5:9])
print("my_data[:-5]",my_data[:-5])
print("my_data[-5:-2]",my_data[-5:-2])

#Concatenation

"""data2 = {40,50,60}
data3 = my_data+data2
print(data3)"""

#multiplication
"""data4 = my_data*2
print(data4)"""

#membership Testing
print(10 in my_data)
print(100 in my_data)
print(10 not in my_data)
