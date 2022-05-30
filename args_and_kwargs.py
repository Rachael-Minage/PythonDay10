# Passing a list or a set to a function

from unittest import result


def addition(numbers):
    result = 0
    for num in numbers:
        result+=num
    return result

num_list = [45,89,98,56,70]
print(addition(num_list))
# *args - Allows you to pass a varying 
# of positional arguments
# use the unpacking operator*

def add(*args):
    result = 0
    for num in args:
        result+=num
    return result

print(add(1,2,3,4,5,6,7,8,9,8,7))

# kwargs - Accepts named or keyword arguments
# Uses **

def joiner(**words):
    result = ""
    for word in words.values():
        result+=word
    return result

print(joiner(a="Real", b="Python", c="is", d="Great"))

# Unpacking iterables using the asterisk operator
# standard list
list_one = [10,13,34,54,67]
print(*list_one)

def summation(*numbers):
    result = 0
    for num in numbers:
        result+=num
    return result

list1= [1,2,3,4,5]
list2 = [8,6,9]
list3 = [12,14,19]
print(summation(*list1,*list2,*list3))

list_dos = [12,13,14,15,17,19,67,56]
a,*b,c = list_dos
print(a)
print(b)
print(c)
# Merging lists
first_list = [4,5,6,7]
second_list = [8,9,10,11]
third_list = [1,2,3]
merged_list= (*first_list,*second_list,*third_list)
print(merged_list)
# Unpacking operator can also unpack a string,dictionary etc


# Write a function that accepts any 
# number of integers as positional arguments and any number of
#  keyword arguments as 
# students' attributes (name, age, country, class) and prints
#  the result of multiplying all of the integers with
#  a greeting based on the student attributes given.
