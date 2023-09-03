contacts = [
    {
        "name":"Jonnathan",
        "phone":"99880 12345",
        "conversation":[
            "hi",
            'Hello',
            'This is awesome day',
            "Lets go and play"
        ]
    },
    {
        "name":"Fionna",
        "phone":"99110 12345",
        "conversation":[
            "hi ji",
            'Whats up',
            'How \'s your  day',
            "Lets go and have coffee together"
        ]
    },
    {
        "name":"George",
        "phone":"99880 12345",
        "conversation":[
            "Sat sri akal",
            'Same To you',
            'This is awesome day',
            "Oh Yeah"
        ]
    }

]

search_keyword = input("ENter kewyord to search")

for contact in contacts:
    """if contact["name"].lower().startswith(search_keyword.lower()):"""
    if contact["name"].lower().find(search_keyword.lower())>=0\
        or contact["phone"].find(search_keyword) >=0\
            or contact["conversation"].find(search_keyword)>=0:

        print(contact)
        print("~~~~~~~~~~~~")
    """else:
        print("Sorry! Not Found")"""
