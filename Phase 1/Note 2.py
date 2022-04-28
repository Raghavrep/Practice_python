import math as m   # With this we can use all math functions , given below are few examples
x=m.sqrt(25)
y=m.ceil(2.6)
z=m.floor(2.6)
print(x,'--',y,'--',z)

# if you dont want to import whole set of math fucntions then you can fetch specific functions

#from math import pow,sqrt         ---- using this line you can use only pow and sqrt function from math library


#  if , elif , else


# a=int(input("enter first number"))
# b=int(input("enter second number"))
# if a + b > 10 :
#     print('number is greater then 10')
# elif a + b == 10 :
#     print('Number is perfect 10')
# else :
#     print('number is smaller than 10')

# While loop
# loop= int(input('enter the number to print your first name'))
# while loop>=1 :
#     print('raghav',end="")
#     loop2 = 4
#     while loop2 >=1 :
#         print('sharma', end="")
#         loop2=loop2-1
#     loop=loop-1
#     print()  # for new line


# For loop is used for sewuence generation
# Example 1
x=[23,41,'raghv']
for i in x:
    print(i)

# Example 2
for j in range(1,21,2):  # syntax for j in range(starting point , ending point , gap)
    print(j)
