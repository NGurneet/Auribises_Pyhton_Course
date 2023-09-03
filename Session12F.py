name = "john"
age = 30
email = "john@example.com"

contact = {
    "name": "jerry",
    "age": 30,
    "email": "john@example.com"
}

print(name, age, email)
print("Name: {} | Age: {} | Email:{}".format(name,age,email))
print()
print("Name: {0} | Age: {1} | Email:{2}".format(name,age,email))

print("Name: {0} | Age: {1} | Email:{2}".format(name,age,email))
print("name:{nm} age:{ag} email:{em}".format(nm=name, ag=age, em=email))

print("Name: {name} | Age: {age} | Email: {email}".format_map(contact))