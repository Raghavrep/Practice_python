print('c:\home\new') # it will use \n as a new line but if we want to not let any defined func work here we use raw
print(r'c:\home\new') # adding r before the actual string will make th ecompiler use it in raw form only

# / - divison , it can divide and give float values as well
# // - floor division , it will give round off integer value only

# set is defined in {}
# list is defined in []
# tuple is defined in ()

name = 'Raghav'   #defining variable
jumblr = name[0] + name[2] + name [4]   #taking the character using string index -- strts from 0
print(jumblr)
conct= jumblr + 'Sharma'
print(conct)

# String is immutable , means it cannot change once assigned -- example you cant write name [0:3]='my',
# it will throw an error stating that string doesnt support item assignment
print(len(name))  # len is used to find the length of string

# Working with Lists --- set of items that are mutable --- Most important point-- List is defined in []
list = [9.3,'raghav',11]
print(list)
list.append(23)
print(list)
list.remove(23)
print(list)
list.insert(2,10000)
print(list)
list1 = [88,311,454,111,222,333,444]
print(list1)
final_list= list + list1   #adding 2 lists
print(final_list)
final_list2 = [list, list1]    # putting lists in list
print(final_list2)

#stat1 = [min(list),max(list),sum(list)]
minimum=min(list1)  # min max and sum , thse are some inbuilt functions that can be used in list to get some vals
print(minimum)

list1.sort()
print(list1)
# learnings -- you cannot put the sorted output in some variable ,
# if you have sorted a list,directly print that list


# Tuple is a type of list but it is immutable i.e once tuple is created it cant be modified.
example_tuple = (12,34,23,'raghav')
print(example_tuple)  # thats all , rest using built in function we can only find count and index
# ---max , min , sort nothin will work for typle

# Last is set , elements are defined in same way we do in list but it doesnt care about indexs ,
# it uses hash to store the values, this way it fetches the data faster
example_set = {23,31,12,267,'raghV'}
print(example_set)


# Dictionary in python
# we can enter a key value pair , so that whenever key is called it returns the value
# Example
dictionary = {1:'Raghav',2:'ram',4:'rohit'}
print(dictionary[2])   # returns the values associated with key number 2
#print(dictionary[3])   #this will throw an error because key number 3 in not present in our dictionary

# there is one more way of calling the key
print(dictionary.get(1 ,'not found'))  # get func works in if else kind of pattern
print(dictionary.get(3 ,'not found'))  # where it couldnt find the key , it return the string as else statement

# we can use dict func to make key and values from defined lists
#example
key= [1,2,3,4,5,6,7]
values = ['a','b','c','d','e','f','g']
data=dict(zip(key,values))
print(data)

# Method of swapping the value of 2 variables
a=2
b=8

a,b=b,a      # method of swapping the values  now a =8 and b =2s
print(a,b)