# number = [5, 2, 8, 1, 9]
# number.sort(reverse=True)
# print(number)  # Output: [9, 8, 5, 2, 1]

# number = sorted([5, 2, 8, 1, 9])    
# sorted_li=sorted(number)
# print(sorted_li) 
# print(sorted) # Output: [1, 2, 5, 8]
# # Output: [1, 2, 5, 8, 9]

# # list comprehension 
# # can be written as li=[]
# li = []
# for i in range(1,6):
#     li.append(i*i)
# print(li)  # Output: [1, 4, 9, 16, 25]

# # or can be completed in only 2 lines like below
# squared = [x**2 for x in range(5)]
# print(squared)  # Output: [0, 1, 4, 9, 16]

# # even no in list
# num=[1,2,3,4,5,6,7,8,9,10]
# even=[i for i in num if i%2==0]
# print(even)  # Output: [2, 4, 6, 8, 10]

# # upper function
# fruits=["apple","banana","cherry"]
# upper_fruits=[i.upper() for i in fruits]    
# print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# # print only digits from string
# text="veyuvgrqg3f7t5478t6"
# digits=[i for i in text if i.isdigit()]
# print(digits)  # Output: ['3', '7', '5', '4', '7', '8', '6']

# # first letter from each word
# scentence="python is very easy to learn"
# first= [i[0] for i in scentence.split()]
# print(first)  # Output: ['p', 'i', 'v', 'e', 't', 'l']


# # seperate vovles
# text="WhiteBoard"
# text1=[i for i in text if i in 'aeiou']
# print(text1)

# # 1 to 10 even number suqare of all
# squared_even=[i**2 for i in range(1,11) if i%2==0]
# print(squared_even)  # Output: [4, 16, 36, 64, 100]

# # print the given string in reverse order
# sentence="learn python easily"
# reverse_order=[i[::-1] for i in sentence.split()]
# print(reverse_order)  # Output: ['easily', 'python', 'learn']

# # print squares in form of (1,1)(2,4) till 5
# squared_tuples=[(i,i**2) for i in range(1,6)]
# print(squared_tuples) # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# # print the letter with has length more than 3
# sentence="this is a test scentence"
# word=[i for i in sentence.split() if len(i)>3]
# print(word)  # Output: ['this', 'test', 'scentence']

# # only print integer from list using type function
# items=[1,"hello",3.5,5,"world"]
# integer=[i for i in items if type(i)==int]
# print(integer)  # Output: [1, 5]

# # print ascii value
# char=['A','B','C']
# ascii_values=[ord(i) for i in char]
# print(ascii_values)  # Output: [65, 66, 67]

# # return in dictionary
# keys=['a','b','c']
# values=[1,2,3]
# dictionary={k:v for k,v in zip(keys,values)}
# print(dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3}

# # palindrome number from list
# list=["madam","racecar","apple","noon"]
# palindrome=[i for i in list if i==i[::-1]]
# print(palindrome)  # Output: ['madam', 'racecar', 'noon']

# # min and max
# # numbers=[10,3,6,2,8,4]
# # min_number=min(numbers)
# # max_number=max(numbers)
# # print(min_number)  # Output: 2
# # print(max_number)  # Output: 10

# # x=["Raj","Vishal","a"]
# # min_number=min(x)
# # max_number=max(x)
# # print(min_number)  
# # print(max_number)

# # # max length string
# # x=["Raj","Vishal","a"]
# # max_length=max(x,key=len)
# # print(max_length)  # Output: Vishal

# # finding max value using for 
# x=[4,5,7,89,12,90,34]
# max=x[0]
# for i in x:
#     if i>max:
#         max=i
# print(max)

# # 
# a=[10,20,30,40,50]
# if 50 in a:
#     print("yes")  # Output: yes
# else:
#     print("no")     

    # copy method
a=[10,20,30]
b=a.copy()
c=b
print(a)
print(b)
print(c)    

# split()converts string to list
text="hello world"
words=text.split()  
print(words)  # Output: ['hello', 'world']

# join function
words_list = ['hello', 'world']
sentence = ' '.join(words_list)
print(sentence)  # Output: hello world