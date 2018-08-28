# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:38:24 2018

@author: Falah Hasan
"""
print("First Line")
print("Second Line")
print("Third Line")

filename = "Weather"
table =  "temprature"
year = "1901"

"""" concatenating three varibales"""
filename+"_"+table+"_"+year
realYear = "1901"

"""" sybtax for IF-ELse statement"""

if year == realYear:
    print("EQUAL")
    print("yes really")
else:
    print("NOT EQUAL")
    print("Check those Values again")
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""" how to create a user defined function""""

def potatoCost (potatoPrice, amount, potatoType):
    cost = potatoPrice*amount
    print(potatoType)
    return(cost)

"""" calling the function potatoCost""""
potatoCost(10,10,3.0)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
converter fundtion to convert miles to kms, using a user defined function
"""
def converterFunc(miles):
    kms = miles*1.609334
    return(kms)

"""" calling the function created""""
mile = 10
converterFunc(mile)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
calcualte area of rectangle, using a user defined function
"""
def areaRectangle(w,b):
    area = w*b
    return(area)


"""" calling the function created""""
areaRectangle(4,5)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
concatenate two names using a user defined function

"""
def concatenatName(first, last):
    name = first+" "+last
    return(name)


"""" calling the function created""""
first = "John"
last = "Smith"
concatenatName(first,last)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
list and topples to create sequences
"""

"""creating a list""""
fileList = [2015,2016,2017]
print(fileList)

"""" appending values to a list """
fileList.append(2018)
print(fileList)

"""listing the vlaue atr index 2"""
fileList[2]

"""creating a tuple """"
fileTuple = (2015,2016,2017,2018)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
sets
"""
fileList = [2015,2017,2016,2017]

 """converting the list to set"""
fileSet = set(fileList)
print(fileSet)

 """ creating  a file Dictionary"""
fileDict = {"last year":2017, "present year":2018, "next year":2019}
 """ keys and values"""
 """ displaying the values at for repective keys"""
fileDict["next year"]
fileDict["last year"]
fileDict["present year"]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
""""
fileList = list(range(2000,2020,2))
print(fileList)
fileList[2]
"""
show value at index 2
"""

fileList[:6]
"""
show values before index 6
"""

fileList[2:]
"""
show values from index 2
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""
Iterations
"""
for item in fileList:
    print(item)

for item in range(2010,2030,2):
    print(item)

""""
iterating thorugh the values betweeen 2010 to 2030, every two years. Applyin IF ELSE statements in the iteration
"""    
for item in range(2010,2030,2):
    if item==2020:
        print(item)
    else:
        print(item)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""
working with files
"""
""""
writing text in the files
"""
file = open("E:\\Python Beginers\\hi.txt", 'w')

file.write("Hi there")

""""
reading the new line written in file
"""
file = open("E:\\Python Beginers\\hi.txt", 'r')
content = file.read()
print(content)

""""
appending new line to file
"""
file = open("E:\\Python Beginers\\hi.txt", 'a')
file.write("New Line appended")

"""" closing the file """
file.close()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
