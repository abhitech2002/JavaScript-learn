# list is used to store multiple items in a single variable

# create a list

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ("abc", 34, True, 40, "male")

print(list1)
print(list2)
print(list3)
print(list4)
print("DataType of list4 is:",type(list4))
# list length is the number of items in a list

print(len(list1))

print(list1[0])
print(list1[1])
print(list1[1:2])

if "apple" in list1:
    print("Yes, 'apple' is in the list")

print("Below method are the list methods:")
list1.insert(2, "watermelon")
print(list1)

list2.insert(0, "strawberry")
print(list2)

list3.append("strawberry")
print(list3)

list1.remove("banana")
print(list1)

list1.extend(list2)
print(list1)

del list4
# print(list4) deleted the list

# Loop through the list

for x in list1:
    print(x)

for i in range (len(list2)):
    print(list1[i])

i = 0
while i < len(list1):
    print(list1[i])
    i = i + 1

newlist = [x for x in range(10) if x < 5]

print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

mylist = list1[:]
print(mylist)

result = list1 + list2 + list3
print(result)
# list items are ordered, changeable and allow duplicate values

# The list is chanheable, meaning the we can change, add or remove items in a list after it has been created.

# List, Tuple, Set, Dictionary this all are the python collection (Arrays)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "color": ["red", "white", "blue"]
}

print(thisdict["year"])
print(thisdict)
print(thisdict.get("model"))
print(len(thisdict))
print(thisdict.keys())
print(thisdict.values())
print(thisdict["color"][1])
print(thisdict.items())

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict["year"] = 2018
print(thisdict)

thisdict.update({"color": "red"})
print(thisdict)