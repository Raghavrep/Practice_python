## OOP -- Object oriented programming
#functions in OOP are called methods

# class computer:
#     def config(self):
#         self.name='Ryzen'
#         self.model='AMD radeon'
#     def __init__(self):                # we dnt need to define init , it will be executed everytime we run this code
#         print("Calling itself everytime this code is executed")
#
#
# com1=computer()
# com1.config()
# print(com1.name)
# print(com1.model)

#####################################################################################################################

# understanding class variables and instance variable .

class car:
    wheels=4

    def __init__(self):
        self.brand="BMW"
        self.type='sedan'

c1=car()
c2=car()
c1.brand='Mercedes'    # instance variable , we can change it for c1 or c2
car.wheels=6           # class variable also known as statis variable , when we change it , it changes everywhere c1 as well as c2
print(c1.brand,c1.type,c1.wheels)
print(c2.brand,c2.type,c2.wheels)