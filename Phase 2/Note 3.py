#  Decorators
# Using decorators we can add an extra feature to an existing function without hampering the already existing code .
#
# def div(a,b):        # this is our primary function to divide 2 numbers but we want to add a feature to make a as bigger number always
#     print(a/b)
#
# def smart_div(func): # here we are creating a new function which is calling func within
#     def inner(a,b):  # This is a function within function
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
#
# new_div = smart_div(div)         # this is decorator, here we defined func=div
#
# new_div(2,4)

########################################################################################################################

## Modules --just like numpy we can import the other .py file as module and utilize the functions defined in that .py file as well

import Calculator

c= Calculator.addition(2,3)
d= Calculator.subtraction(2,3)
e= Calculator.multiply(2,3)
f= Calculator.divide(2,3)
print(c)
print(d)
print(e)
print(f)
print("this value was already present here "+ __name__) # this one shows main when print and the one coming from calculator gives module name
###### __name__ it can be used in modules to get the hint that which all modules are being used in our code .
