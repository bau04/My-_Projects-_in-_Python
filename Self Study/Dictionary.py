# Dictionary is one of the advanced datatypes like lists, sets, and tuples
# dict or dictionary are collections of key pairs
#  that are unordered, changeable, and indexed

# dict syntax is: identifier = {
# key1 : value1,
# key2 : value2,
# key3 : value3 }

studentOne = {
     "name" : "Damian",
     "course": "BSIT",
     "age" : 32
}

studentTwo = {
     "name" : "Austin",
     "course": "BSCS",
     "age" : 24
}

print("Dictionary : ", studentOne)  # reads the whole dictionary
print("Dictionary : ", studentTwo)  # reads the whole dictionary

# specify the key'[]' value to read dictionary item
print("Specific Dictionary : ", studentOne["name"])

# using "get(key)" to read a specific dictionary value
print("Get key : ", studentTwo.get("name"))

# assign dictionary items using the "=" operator
studentTwo["name"] = "Jimmy"
print("Reassigned name from damian to Jimmy : ", studentTwo["name"])

# checking dictionary length "len(dictionary)" ; 1 length per key
print("Key length : ", len(studentOne))

# you can add items on a dict by assigning  a non-existent key value
studentOne["Gender"] = "Male"
studentTwo["Gender"] = "Male"
print("Updated dictionary : ", studentOne)
print("Updated dictionary : ", studentTwo)

# delete using "dictionary.pop(key)"
studentOne.pop("name")
print("pop deleted the name : ", studentOne)

# delete last key using "dictionary.popitem(key)"
studentTwo.popitem()
print("popitem deleted the last: ", studentTwo)

# "dictionary.clear()" deletes ALL THE ITEMS in the dictionary

# "copy()" copies the dictionary to a new dictionary
band1 = {
     "guitarist" : "George",
     "drummer" : "Ringo"
}

band2 = band1.copy()  # copies band1 values to band2
print("copy : ", band2)

# "dictionary.keys()" returns a list that contains all the keys in the dictionary
print("studentTwo keys : ", studentTwo.keys())

# "dictionary.values()" returns a list that contains all the values in the dictionary
print("studentTwo values : ", studentTwo.values())

print("")
# list of dictionaries are dictionaries inside a list
playerOne = {
     "name" : "Darwin",
     "position": "Striker",
     "age" : 24
}

playerTwo = {
     "name" : "Neymar",
     "position": "Forward",
     "age" : 31
}

players = [playerOne, playerTwo]  # converts dictionaries inside a list
print("dictionaries in list : ", players)  # shows dictionaries inside a list

# getting a specific value in a list of dictionaries :  "list[index].get(dictKey)"
print("specific value in a dictionary list : ", players[0].get("name"))

# nested dictionary : dictionary inside a dictionary
playerThreeAttributes = {
     "height" : 185,
     "weight" : 84,
     "nationality" : "Portuguese"
}

playerThree = {
     "name" : "Cristiano",
     "position" : "Forward",
     "age" : 38,
     "physical" : playerThreeAttributes  # "playerThreeAttributes" dict is inside playerThree dict
}

print("Accessing attributes dict inside playerThree dict : ", playerThree.get("physical"))
print("key inside attributes dict inside playerThree dict: ",playerThree.get("physical").get("nationality"))
