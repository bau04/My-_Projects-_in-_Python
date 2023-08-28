# Sets are a collection of variables that is partially writable
# Sets are unordered and unindexed
# You can only add but not edit the values

evenNumbers = {2, 4, 6, 8, 10}
print(evenNumbers)

# Sets cannot be read individually
# You will need to cast the set to a list or a tuple

# "len(set)" is used to check the number of items in a set
print("Length : ", len(evenNumbers))

# "add()" adds an item at the end of the set
evenNumbers.add(12)
print(evenNumbers)

# "update()" is used to add multiple items to a set at the same time
evenNumbers.update([14, 16, 18, 20])
print("update : ", evenNumbers)

# "remove()" is used to remove an item based on their value
# *error if you remove an item that is not in the set
evenNumbers.remove(6)
print("remove : ", evenNumbers)

# "discard()" is used to remove an item based on their value
# NOT an error if you remove an item that is not in the set
evenNumbers.discard(11)
print("discard : ", evenNumbers)

# "pop()" deletes the first item in the set
evenNumbers.pop()
print("pop : ", evenNumbers)

# "clear()" deletes all the value in the set
evenNumbers.clear()
print("clear : ", evenNumbers)

# "copy()" is used to copy the whole set and be assigned to a new set
namesOne = {"Jim", "Vic", "Bob"}
namesCopy = namesOne.copy()
print(namesCopy)

# "union()" returns a set containing all the values of the two sets
setOne = {0, 1, 3, 5, 7, 9}
setTwo = {0, 2, 4, 6, 8, 10}
# combines the duplicated value in the set
setThree = setOne.union(setTwo)
print(setThree)

# "difference()" returns a set containing the values that only exists on the left set not right set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
set3 = set1.difference(set2)
print("Difference : ", set3)

# "intersection()" returns a set containing the values that exists both on two sets
set4 = set2.intersection(set1)
print("Intersection : ", set4)

# "symmetric_difference()" returns a set containing all the values that EXCLUSIVELY exists on each set
setUno = {1, 2, 3, 4, 5}
setDos = {3, 4, 5, 6, 7}
setTres = setDos.symmetric_difference(setUno)
print("Symmetric Difference : ", setTres)

# "isDisjoint()" returns a boolean whether the two sets have an intersection or not
# False when at least one is the same between two sets
print("isDisjoint : ", setUno.isdisjoint(setDos))

# "issubset()" returns a boolean whether the left set is contained in the right set
# False if one value in the right set is not in the left set
print("isSubset : ", set1.issubset(set2))

# "issuperset()" returns a boolean whether the right set is contained in the left set
print("isSuperset : ", set1.issuperset(set2))

# casting Sets
last = {1, 11, 2, 22, 3, 33}
print("last is a set: ", last)  # {} are sets

lastList = list(last)  # converts set to list, [] are list
print("last is list", lastList)

lastTuple = tuple(last)  # converts the set "last" that is now a list to tuple
print("last is now a tuple : ", lastTuple)
