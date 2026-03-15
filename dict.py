''' Dictionaries in Python '''

# A dictionary is an {unordered}, {mutable} collection of {key-value pairs}. Each key in a dictionary is {unique} and is used to access the corresponding value. Dictionaries are defined by placing a comma-separated sequence of key-value pairs within {curly braces} `{}`, with a colon `:` separating each key and value.

''' Creating Dictionaries '''

# Empty Dictionary-;.

empty_dict = {}


# Dictionary with Elements

person = {
    "name": "Manav",
    "age": 21,
    "profession": "Engineer"
}
print(person)


# Using the `dict()` Function

person = dict(name="Manav", age=21, profession="Engineer")
print(person)


''' Features of Dictionaries '''

# 1. Key-Value Pairs
# Dictionaries store data in key-value pairs, allowing you to efficiently retrieve, add, and modify values based on their keys.


person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}
person['name'] = 'Manav'
print(person["name"])  # Output: 'Alice'


# 2. Unordered
# Dictionaries do not maintain the order of elements. From Python 3.7 onwards, dictionaries maintain the insertion order as an implementation detail, but this is not a guarantee for all Python versions.


person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'profession': 'Engineer'}


# 3. Mutable
# Dictionaries can be modified after creation. You can add, update, and remove key-value pairs.


person = {"name": "Alice", "age": 30}
print(person)
person["profession"] = "Engineer"  # Adding a new key-value pair
person["age"] = 31                 # Updating an existing value
print(person)  # Output: {'name': 'Alice', 'age': 31, 'profession': 'Engineer'}


# 4. Dynamic Size
# Dictionaries can grow and shrink in size as elements are added or removed.

''' Common Dictionary Operations '''

# Accessing Values
# You can access values by their keys using square brackets `[]`.


person = {"name": "Alice", "age": 30}
print(person["name"])  # Output: 'Alice'


# Adding and Updating Values
# You can add new key-value pairs or update existing ones.


person = {"name": "Alice", "age": 30}
person["profession"] = "Engineer"  # Adding a new key-value pair
person["age"] = 31                 # Updating an existing value
print(person)  # Output: {'name': 'Alice', 'age': 31, 'profession': 'Engineer'}


# Removing Key-Value Pairs
# - `del` statement: Removes a key-value pair.

person = {"name": "Alice", 'age': 30}
del person["age"]
print(person)  # Output: {'name': 'Alice'}


# - `pop()`: Removes a key and returns the corresponding value.

person = {"name": "Alice", "age": 30}
age = person.pop("age")
print(age)     # Output: 30
print(person)  # Output: {'name': 'Alice'}


# - `clear()`: Removes all key-value pairs from the dictionary.

person = {"name": "Alice", "age": 30}
person.clear()
print(person)  # Output: {}


''' Dictionary Methods '''

# `keys()`, `values()`, and `items()`
# These methods return views of the dictionary's keys, values, and key-value pairs, respectively.


person = {"name": "Alice", "age": 30}
print(person.keys())    # Output: dict_keys(['name', 'age'])
print(person.values())  # Output: dict_values(['Alice', 30])
print(person.items())   # Output: dict_items([('name', 'Alice'), ('age', 30)])


# `get()`
# Returns the value for a specified key if the key is in the dictionary; otherwise, it returns a default value (e.g., `None`).


person = {"name": "Alice", "age": 30}
print(person.get("name"))       # Output: 'Alice'
print(person.get("profession")) # Output: None
print(person.get("nam","notpresent"))  # Output: 'Unknown'


# `update()`
# Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.

n = "name"
person = {"name": "Alice", "age": 30}
person2 = {n : "Manav", "profession": "Engineer"}
print(person)
person.update(person2)
print(person)  # Output: {'name': 'Alice', 'age': 31, 'profession': 'Engineer'}

''' Iterating Over Dictionaries '''

# You can iterate over dictionaries to access keys, values, or key-value pairs.

# Iterating Over Keys

person = {"name": "Alice", "age": 30}
for k in person.keys():
    print(k)
# Output:
# name
# age


# Iterating Over Values

person = {"name": "Alice", "age": 30}
for v in person.values():
    print(v)
# Output:
# Alice
# 30


# Iterating Over Key-Value Pairs

person = {"name": "Alice", "age": 30}
print(person.items())
for (i,j) in person.items():
    # print(f"{i}: {j}")
    print (f"key : {i}")
    print (f"value : {j}")
# Output:
# name: Alice
# age: 30


''' Practical Uses of Dictionaries '''

# Question : Counting Elements
# Dictionaries are often used to count occurrences of elements in a list.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for w in words:
    word_count[w] = word_count.get(w,0) + 1
    print(word_count) 
    print(f"{w} : {word_count.get(w)}")
print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
    
''' 
    Initially :
            apple : 0
            banana : 0
            orange : 0
        Output of each Iteration :
            apple : 1
            banana : 1
            apple : 2
            orange : 1
            banana : 2
            apple : 3
'''


# Storing Configuration Settings
# Dictionaries are useful for storing configuration settings and options.


config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
name = config["host"]
print(name)

''' Summary 

Dictionaries in Python are powerful and versatile data structures that allow you to store and manipulate key-value pairs. They are useful in a wide range of applications, from simple data storage to complex data manipulation. Understanding dictionaries and their features is essential for effective Python programming. '''
# function with return type
def add(x,y):
    return x+y
# function calling
print("5+6 =",add(5,6))
print("10+20 =",add(10,20))

# passing list as an argument
def fruits(fruitlist):
    for fruit in fruitlist:
        print("I like ", fruit)
mylist = ["apple","banana","mango"]
# function calling 
fruits(mylist)
