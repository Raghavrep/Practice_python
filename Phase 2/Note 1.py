# Arrays
# arrays stores only one type of values , be it integer char or float . unlike list where we can store any type of values
# to create array we need to import the array module

# import array
# vals=array.array('i',[1,2,3,4,5,7,6])          # i here is the type code of array inputs i= unsigned integer
# for i in range(len(vals)):
#     print(vals[i])

# Create an array by giving inputs
# import array
# arr=array.array('i',[])
# length=int(input("enter the length for array"))
#
# for i in range(length):
#     val=int(input("enter the values for array"))
#     arr.append(val)
# print(arr)


## Array cannot be 2 or 3 dimensional, so for that we use numpy module -----
#array()  #linspace()  #logspace()  #arange()  #zeros()  #ones()

# import numpy as num
# arr=num.array('i',[1,2,3],[5,6,7])
# print(arr)
#######################################################################
# import numpy as num
# arr=num.linspace(0,10,5)   # we give start stop and divisions , by default its 50
# print(arr)
########################################################################
# import numpy as num
# arr=num.logspace(1,10,5)   # we give start stop and divisions----it is different thne linspace because it start and stop point will be powers of ten
# print(arr)
########################################################################
# import numpy as num
# arr=num.arange(1,40,5)   # we give start stop and divisions----division here means the gap between elements
# print(arr)
########################################################################
# import numpy as num
# arr=num.zeros(5,int)   # prints zeros only , same is for ones----num.ones
# print(arr)

########################################################################
# multi dimension array

# import numpy as num
# arr=num.array([
#     [1,3,5],
#     [3,6,7]
# ])
# print(arr)
# print(arr.ndim,"dimesional array")  # it will tell the dimesions of array
# print(arr.shape, 'rows and columns')   # gives number of rows and columns

########################################################################
#Functions
# Most simple example for sytax
# def simple():                     #defined
#     print("simple function")      #body
#
# simple()                          #function call