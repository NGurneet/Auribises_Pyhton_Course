quote = "Search the Candle rather than cursing the darkness"
print("len(quote):",len(quote))
#Indexing
print("quote[2]:",quote[2])
print("quote[49]:",quote[49])

#Negative Indexing
print("quote[-1]:",quote[-1])
print("quote[-50]:",quote[-50])
#Slicing
print(quote[:12])
print(quote[4:12])
print("quote[:-13]",quote[:-13])
print(quote[10:])
print("quote[-11:-33]:",quote[-29:-1])


#Concatenation
meaning = " : Always Try to find solution rather than discussing the problem"
full_quote = quote+meaning
print(full_quote)

#Multiplication
print(quote*2)
#Membership Testing
print("Search" in quote)
print("Search the Candle" in quote)
print("Search the Candle" not in quote)