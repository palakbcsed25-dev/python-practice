# Empty Tuple
t0 = ()

# Tuple with Elements
mixed_tuple = (1, "hello", 3.14, True)
nested_tuple = (1, (2, 3), (4, (5, 6)))

# Accessing Element
fruits = ("apple", "banana", "cherry")
# fruits[0] = "mango" 
print(fruits[0])  # Output: 'apple'
print(fruits[-1])  # Output: 'cherry'
print(fruits[1:3])  # Output: ('banana', 'cherry')

for fruit in fruits:
    print(fruit)

# type cast
tuple1 = (1, 2, 3)
print(type(tuple1))
t = list(tuple1)
print(t)
print(type(t))
n = tuple(t)
print(n)
print(type(n))


# Concatenation and Repetition : using the + operator and repeat elements using the * operator.
tuple1 = (1,2,3)
tuple2 = (4, 5, 3)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)


tuple1 = (1, 3)
repeat_tuple = tuple1 * 3
print(repeat_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# count()
print(repeat_tuple.count(3))  # Output: 3

# index()
print(repeat_tuple.index(3))  # Output: 1