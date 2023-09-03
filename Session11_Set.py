#Explore Set

john_followers = {"fionna","jake","jack","joe","george"}
fionna_followers = {"jack","joe","george"}
jake_followers = {"fiza","sem","john","joe","gerimi"}
print(john_followers,type(john_followers))

numbers = list(range(10,101,10))
print(numbers,type(numbers))

numbers = set(numbers)
print("numbers now:",numbers)
print(numbers,type(numbers))

numbers.add(10)
numbers.add(110)
numbers.add(20)
numbers.add(220)

print("numbers after add:",numbers)
numbers.pop()
print("numbers after pop:",numbers)
numbers.pop()
print("numbers after pop:",numbers)

numbers.remove(50)
numbers.discard(30)
print("Numbers after remove and discard:",numbers)
mutual_followers = jake_followers.intersection(jake_followers)

print(mutual_followers)
print(fionna_followers.issubset(john_followers))
print(fionna_followers.issuperset(john_followers))

A={1,2,3,4,5}
B = {4,5,6,7,8}
print("A: ",A,"B: ",B)
C = A -B
print("C is:",C )
D= A&B
print("D is:",D)

E = A^B
print("E is:",E )
F = A|B
print("f is:",F )

"""#Explore What is symmetric_difference
G = A.symmetric_difference()"""