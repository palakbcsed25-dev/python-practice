# # functions in python
# def msg():
#     print("Hello World")    
# msg()

# def add():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     sum=a+b
#     print(sum)
# add()

# add function
# def add(a,b):
#     print(a+b)
# add(int(input()),int(input()))

# def add(a,b,c=None):
#     if c==None:
#         print("sum of 2 numbers:",a+b)
#     else:
#         print("sum of 3 numbers:",a+b+c)
# add(2,3)
# add(2,3,4)

# # keyword only argument
# def add(*,a,b,c=None):
#     if c==None:
#         print("sum of 2 numbers:",a+b)
#     else:
#         print("sum of 3 numbers:",a+b+c)
# add(a=2,b=3)
# add(a=2,b=3,c=4)

# varible argument
# def add(*a):
#     print(a)
# add(2,3,4,5,6,7,8,9)    

# keywords argument
# def person(**info):
#     print(info) 
# person(name="Manav",age=21)

# positional only argument
def fun(x, /, y):
    print(x,y)
 fun(i=10,y=20) # error

