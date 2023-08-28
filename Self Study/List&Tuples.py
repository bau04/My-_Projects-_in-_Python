# Lists = read and write collection of variables // similar to array in java*

# +INDEX -   0       1        2
# -INDEX -  -3      -2       -1
name = ["LeBron", "Kevin", "Steph"]

print("List : ", name[0])
print("List : ", name[-3])

# reading lists range

#         0      1     2      3      4
Yeses = ["oo", "si", "yes", "oui", "ja"]
# end index is excluded
print(Yeses[1:])  # si to ja
print(Yeses[:4])  # oo to oui *"ja is excluded because last index is excluded"
print(Yeses[1:3])  # si to yes

# Changing name index 1 value from "Kevin" to "Joel"
name[1] = "Joel"
print("List value change: ", name[1])

# list Length
print("list length : ", len(Yeses))

# use "indexName.count(v)" to count how many times an item occurs

# use "list.append" to add an item at the end of the list
name.append("Luka")  # before, there was no third variable now it's luka as it's been added
print("list append : ", name)

# use "list.insert(index, value)" to add an item to a specific index
name.insert(1, "Nikola")
print("list insert : ", name)

# use "list.remove(value)" to remove an item based on their value
name.remove("Nikola")
print("list remove : ", name)

# use pop() -> "list.pop(index)" to remove an item based on index.
# Deletes the last if index is not specified
name.pop(3)
print("list pop : ", name)

#  use del() -> del list[index] to delete based on index.
#  If index is not specified, it deletes the whole list
del name[2]
print("list delete : ", name)

# "list.clear()" deletes all the values in the list

# copy() copies the whole list
nameTwo = name.copy()
print("list copy : ", nameTwo)

# use "+" to combine two lists
Beat = ["John", "Paul"]
les = ["George", "Ringo"]
Beatles = Beat + les
print("using '+' in list : ", Beatles)

# "extend()" combine 2 lists by appending the specified list to the end of first list
# listOne.extend(listTwo)
Beat.extend(les)
print("list extend : ", Beat)

# "reverse()" reverses the value of the list
Beatles.reverse()
print("reverse list : ", Beatles)

# "list.sort()" lists items by alphabet or value
alphabet = ["M", "X", "R", "A", "K"]
alphabet.sort()
print("sort list : ", alphabet)

# "list.sort(reverse)" lists items in reverse order by alphabet or value
num = [3, 5, 2, 1, 4]
num.sort(reverse=True)
print("reverse sort list : ", num)

# nested lists = a list inside a list
# index are    0           1                2
Sports = ["Football", "Basketball", ["MMA", "Boxing"]]
# to access sub list
print("nested lists : ", Sports[2][0])  # first index is to get the index of the sublist and the second is for the
# specific value


# Tuples = similar to lists but read only "tuple = ()"
# CAN be read, combined, and deleted completely
# CAN'T be assigned or deleted one by one
course = ("BSIT", "BSCS", "BSN")
print("tuples : ", course[0])

# converting tuples and lists
print("course is a tuple : ", course)
course = list(course)  # course is now a list
print("course is converted to list : ", course)
course = tuple(course)  # course is back to tuple
print("course is converted back to a tuple : ", course)
