# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# Grater than
a = 33
b = 200
if b > a:
    print("b is greater than a")


# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


# Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short Hand If....Else
a = 2
b = 330
print("A") if a > b else print("B")

# Creating a function
def my_function():
   print("Hello from a function")

my_function()


# Function with arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arbitary Arguquent
def my_function(*kids):
   print("the youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1="mansi", child2="diya", child3="pratibha")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# lambda function
x = lambda a, b : a * b
print(x(5, 6))
