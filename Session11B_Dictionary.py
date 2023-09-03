#my_tuple = ()
my_tuple = tuple()
print(my_tuple)
my_list = list()
print(my_list)
my_set = set()
print(my_set)
my_dict = dict()
print(my_dict)

my_data ={
    101:"John",
    201:"Fionna",
    301:"George",
    601:"Marry"


}
print("my_data")
print(my_data)
print("Min",min(my_data))
print("Max",max(my_data))
print("Sum",sum(my_data))

print("my_data[201]:",my_data[201])
print("my_data.get(201):",my_data.get(201))
my_data.pop(201)
print(my_data)
#del my_data[601]
#my_data.remove[101] Error
my_data[775] = "Leo"
print(my_data)
my_data[775] = "kim"
print(my_data)
del my_data[775]

columns = ["Ludhiana","Ferozpur","Jalandhar","Amritsar"]
population = {}.fromkeys(columns,"12000")
print(population)
population["Ferozpur"] = 32000
print(population)
#Convert Dict into list of tuples
items = list(population.items())
print("items")
print(items)