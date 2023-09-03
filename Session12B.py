#Strings are immutable :)
names = "John,Jennie,Jim,Jack,Joe"
print(names)
upper_case_names = names.upper()
print(upper_case_names)
print(upper_case_names.isupper())

s1 = names.capitalize()
s2 = names.title()
s3 = names.swapcase()
s4 = names.replace('J','K')
print("s1",s1)
print("s2",s2)
print("s3",s3)
print("s4",s4)
password = input("ENter the password: ")
print("password: ",password.strip())

data = "00000003045"
print("data:", data.strip('0'))

num = 3.5600000000
num = float(str(num).strip('0'))
print(num,type(num))

message = "No internet Connectivity"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

data = "545"
print(data.zfill(30))

quote = "Search the Candle rather than cursing the darkness"
print(quote.find('sing'))
print(quote.find('the'))
print(quote.index('the'))
print(quote.index('the'))
print(quote.rindex('the'))
print(quote.index('Candle'))
print(quote.rindex('Candle'))

idx1 = quote.index('Candle')
idx2 = idx1+ len('Candle')-1
print(idx2)
