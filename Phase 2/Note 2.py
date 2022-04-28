####  Fibonacci series  ####
# def fib(n):
#     a=0
#     b=1
#
#     print(a)
#     print(b)
#
#     for i in range(2,n):    # strting from 2 because a and b are defined
#         c=a+b
#         a=b
#         b=c
#         print(c)
#
# fib(5)

#######################################################################################
# finding the factorial of a number
# def factorial(n):
#     for i in range(1,n):
#         n=n*i
#
#     print(n)
#
# factorial(5)
#######################################################################################

# Basics of recursion - WHen a function is called within function , it is known as recursive function
# def greet():
#     print('Good morning')
#     greet()
#
# greet()      # it stops after limit of 100
#######################################################################################
# recreting factorial function but this time we will use concept of recursion
# def fact(n):
#     if n==0:
#         return 1
#     return n * fact(n-1)
#
#
# result=fact(5)
# print(result)

#######################################################################################
# whenever we want to create a function but it wont be used alot , then we can go for anonymous function called lambda

# f= lambda a,b :a+b
# result= f(2,3)
# print(result)
#######################################################################################
# filter # map     # reduce

from functools import reduce

lst=[1,2,3,4,5,6,7,7,8]
find_even = list(filter(lambda a: a%2==0,lst))    # filter is used to find some specific values
print(find_even)
make_double=list(map(lambda b:b*2,find_even))     # to apply function to all elements
print(make_double)
add_all=reduce(lambda x,y:x+y,make_double)        # reduce is used to implement any changes using all elements in list with each other.
print(add_all)














