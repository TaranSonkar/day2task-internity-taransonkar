#INDEXING WITH SEQUENCE
'''index into a sequence is to retrieve a single member by specifying an integer index
that indicates the place of that member in the sequence:seq[index].
Python uses a zero-based indexing system, meaning that the first element in a sequence is located at position 0.'''


#string indexing:

a='internity'
print(a[0])

#output--i

print(a[0],a[3])

#output--i e

print(a[0:5])

#output--inter

print(a[0:])

#output--internity

print(a[:-1])

#output--internit

print(a[0:5:2])

#output--itr

#################################################################################

#list indexing

a=[1,2,'hello',(3,4),{'key':'value'}]

print(a[0])

#output--1

print(a[0],a[3])
#output--1 (3, 4)

print(a[0:5])
#output--[1, 2, 'hello', (3, 4), {'key': 'value'}]
print(a[0:])

#output--[1, 2, 'hello', (3, 4), {'key': 'value'}]
print(a[:-1])

#output--[1, 2, 'hello', (3, 4)]

print(a[0:5:2])
#output--[1, 'hello', {'key': 'value'}]

#####################################################################################

#dictonry indexing

a={'name':'Taran','age':20,'skill':'python with datascince'}

print(a['name'])

#output--Taran

######################################################################################

#Tuple indexing


a=('name',2,2.5)

print(a[0])

#output--name

print(a[0:3])

#output--('name', 2, 2.5)

print(a[0:])

#output--('name', 2, 2.5)

print(a[:1])

#output--('name',)

print(a[0:3:1])

#output--('name', 2.5)

#######################################################################################


#SLICING INDEXING WITH SEQUENCE

'''Slicing in Python is a feature that enables accessing parts of sequences like strings,
tuples,and lists. You can also use them to modify or delete the items of mutable sequences such as lists.
Slices can also be applied on third-party objects like NumPy arrays,
as well as Pandas series and data frames.'''


a = ("a", "b", "c", "d", "e", "f", "g", "h")

print(a[0:8:3])

#output--('a', 'd', 'g')

a='DATALOVES'

print(a[:-2])

#output--DATALOV

a=[2,3,4,5,6,7,8,9]

print(a[3:5])

#output--[5,6]

a=[2,3,4,5]

print(a[2:])

#output--[4,5]

##############################################################################################

#EXCEPTION HANDLING

'''The try and except block in Python is used to catch and handle exceptions.
Python executes code following the try statement as a “normal” part of the program.
The code that follows the except statement is the program's
response to any exceptions in the preceding try clause.'''

#Question1

try:
    x=3
except:
    print('x value is 3')
else:
    print('something went worng')

#output--- something went worng

#Question2
    
try:
    a=float(input("enter a number"))
    b=float(input("enter number"))
    def div(a,b):
        return a/b
    print(div())
except:
    print("can't be divided by zero")
#output--- can't devided by zero you enter the like this 2/0
#you enter 4/2 now answer is 2

#Question3

a=20
try:
    print(a)
except:
    print("somthing went worng")
finally:
    print("welcome to data loves cloud servies")

'''The finally keyword is used in try... except blocks.
It defines a block of code to run when the try... except...else block is final.
The finally block will be executed no matter if the try block raises an error or not.'''

#Question4
try:
    def name(a=int(input("enter a age"))):
        if(a>=18):
            print("you are elder")
        else:
            print("you are minior")
    name()
except:
    print("value error")
else:
    print("something went worng")

#output ---your input according

#Question5
a=2000
if(200<2000):
    raise Exception("sorry the number is 300")

#raise Exception is make a error

#############################################################################################################



#REGULAR EXPRESSION

'''Just to check a pattern maching,we are going to regular expression like how to string accure how many times.'''

#Funtion name
#match(),findall(),pattern(),search()
#module name use re

#regular expression know as Regex

#match()--to check data aviable or not

#search()-- to search the opretion

#findall()-- i want to check intair string or not

#pattern()-- to identfy find the string find the pattern main string.
##################################################################################################################

#Question-1

import re
s=re.match('internity','hi internity')
print(s)

#output--(2,11)

#Question-2

import re
s=re.search('dataloves','how are you student and dataloves begins the training')
print(s)

#output--datalove,26,35

#Question-3

import re
s=re.findall("dataloves","vinit,vishal join dataloves provide services like dataloves cloud")
print(s)
print(tuple(s))
print(set(s))
print(frozenset(s))

#output--['dataloves', 'dataloves']
#('dataloves', 'dataloves')
#{'dataloves'}
#frozenset({'dataloves'})

################################################################################################

#to only print match data

# * zero to more
# + one or more
# ? zero or more
# [a-z] to represent the data (all char from a-z)
# [a-f] only a-f
# [a,b,c] only 3 charachters
# [0-9] digits from 0-9
# [^ abc] not abc remaining all

################################################################################################

#Question 4

import re
r=re.match(r"[a-z]+bh","saurabh sir how are you")
print(r.group())

#output--saurabh

#Question 5

import re
r=re.match(r"[a-z]?an","taran sir how are you")
print(r)

#output--None

#Question 6

import re
r=re.match(r"[a-z]?","taran sir how are you")
print(r)

#output-- <re.Match object; span=(0, 1), match='t'>

#Question 7

import re
r=re.match(r"[a-z]?an","ran sir how are you")
print(r.group())

#output--ran

#Question 8

import re
r=re.search(r"[a,b,c]*soft","saurabh sir how are you datasoft are you")
print(r.group())

#output--asoft

#Question 9

import re
r=re.search(r"[a,b,c,d,e,f]*soft","saurabh sir how are you datasoft are you")
print(r.group())

#output--asoft

#Question 10

import re
r=re.search(r"[a-j]*b","taran sir how are you dabasoft are you")
print(r.group())

#output-- dab

#Question 11

import re
msg='call me at 278323974'
regex=re.compile(r'\d+') # compile is new digit function
nu=regex.search(msg)
print(nu.group())

#output-278323974 







    
    



















