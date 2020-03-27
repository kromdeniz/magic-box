# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:10:20 2020

@author: mnm
"""

#list
#you can out more than one value in a variable in a unique way
#Ex: x = [am,got,meme]
#or x = ["am string","got string","meme string"]
#conceptially in a classroam there is more than one students
#thus classroam is a list


#index
#each element in a list has a position this position is called index
#the index of the first element in a list starts with 0 then increase by 1
#if you wwant to get the value of an element in a list by its index
#you have to write the name of the list
#then inside the third bracket write the value of the index of the element
# x = ["am string","got string","meme string"]
# print(x[2])
#got string

#how to get the index 
#if you are not sure what is the index of an element in a list
#you can write name of the list and then a dot(.)
#after the dot you need to write index
#inside the parantheses you will write the element of which
#you want to find out its index
# x =["am","got","meme"]
# got_index = x.index("got")
# print(got_index)

# x =["am","got","meme"]
# x[1] = "sik"
# print(x)
#["am","sik","meme"]


#list advance
#append
#adding a new element is like appending an element to the list
#to add z in your list you will append the x
# x = ["am","got","meme"]
# x.append("sik")
# print(x)
# ['am', 'got', 'meme', 'sik']


#the total number ina list is called length of the list
#to know the length of a list you use the keyword len
# x = ['am', 'got', 'meme', 'sik']
# count = len(x)
# print(count)
# 4

#to remove from the list you use the keyword remove
# x = ['am', 'got', 'meme', 'sik']
# x.remove("sik")
# print(x)
# ['am', 'got', 'meme']

#to get the lowest number in a list you use the keyword min
# num = [1,3,5,-5]
# print(min(num))
# -5

#to get the highest number you use the keyword max
# num = [1,3,5,-5]
# print(max(num))
# 5

#element exists
#to know wheter an element exists in a list you use the keyword in
#first you write the element name then in then the name of the list
#if element exists in the list you will get True otherwise you will get False
# x = ["am","got","meme"]
# print("meme"in x)
# True

#concat lists
#to combine two lists you use the + sign
# x = [1,5,7]
# z = [2,4,6]
# all_nums = x + z
# print(all_nums)
#[1, 5, 7, 2, 4, 6]

#pop
# to remove the last element from a list you use the keyword pop
# x = [1,3,5,7]
# x.pop()
# print(x)
# [1, 3, 5]

#list sort
#to organize the numbers in a list you can use the keyword sort
# x = [1,3,5,7,-5,2,23,-9]
# x.sort()
# print(x)
# [-9, -5, 1, 2, 3, 5, 7, 23]

#you can sort a list of strings aswell
# x = ["am","got","sik","meme","popo"]
# x.sort()
# print(x)
# ['am', 'got', 'meme', 'popo', 'sik']

#to revers the list and put the last element as the first one 
#you use the keyword reverse
# x = ["am","got","sik","meme","popo"]
# x.reverse()
# print(x)
# ['popo', 'meme', 'sik', 'got', 'am']

#range
#to get a range of numbers you use range() and give a number
#the number you provide is the number where the range will stop
#range(5)
#to start your range not to start from 0 instead start at 7 and stop at 15
#range(7,15)



#for loop
# basket = ["apple","banana","pear","orange"]
# for fruit in basket:
#     print(fruit)
 
#apple
# banana
# pear
# orange

#for loop structure
#1 write the keyword for
# 2 declare loop variable the value of this variable will be each element
# in the list
# 3 write the keyword in
# 4 write the name of the list on which you want to run the for loop then:
# 5 pres tab to indent then write one or more lines that you want to do in rep

#repeat multiline
# basket = ["apple","banana","pear","orange"]
# for fruit in basket:
#     message = "fresh " + fruit
#     print(message)
# fresh apple
# fresh banana
# fresh pear
# fresh orange    

#condition inside a loop
#as you can write more than one line inside a for loop
#you can write a condition there as well
#as in the code below it will print a number is greater than 0
# num_1 = [1,5,9,-6,-18,22]
# for num_2 in num_1:
#     if num_2 > 0:
#         print(num_2)
# 1
# 5
# 9
# 22 

#break
#while running the for loop the code below will hit the break
#when the loop gets a negative number
#this will stop immediately even though there are more elements after
# num_1 = [1,5,-5,14,55]
# for num_2 in num_1:
#     if num_2 < 0:
#         break
#     print(num_2)
# 1
# 5    

#continue
#while running a for loop you can skip some elements by using the continue
#it skips the rest of the iteration for this element
#and goes to the next element
#the code below will skip the even numbers
# num_1 = [1,2,4,5,6,12,15,20,21,36]
# for num_2 in num_1:
#     if num_2 % 2 == 0:
#         continue
#     print(num_2)
# 1
# 5
# 15
# 21    
    
# #the code below will skip the negative numbers
# num_1 = [1,5,-5,11,-25,-18,17,-55]
# for num_2 in num_1:
#     if num_2 < 0:
#         continue
#     print(num_2)
# 1
# 5
# 11
# 17    


#while loop
#while doing something based on a condition you use another kind of loop
#you write a while loop as below
#num = 0
# while num < 5:
#     print(num)
#     num = num + 1
# 0
# 1
# 2
# 3
# 4
    
#to write a while loop you have to do five things
#declare a loop variable
#write the while keyword
#add a stopping condition after the while
#underneath while write the repeating work
#update the loop variable
#if the loop condition becomes True the loop will continue
#if the the condition becomes False the loop will stop running

# num = 0
# while num < 3:
#     print(num)
#     num = num + 1       #this line is to update the variable s value
# 0
# 1
# 2

# num = 0
# while num < 6:
#     print(num)
#     num = num + 2       #this line is to update the variable s value
# 0
# 2
# 4    

# num = 5
# while num > 0:
#     print("fire")
#     num = num - 1
# fire
# fire
# fire
# fire
# fire
    
#to run a while loop to sum all the numbers from 1 to 10
# x = 1
# sum = 0
# while x <= 10:
#     sum = sum + x
#     x = x + 1
# print(sum)    
# 55

#to sum of all even numbers from 1 to 10
#you need to add a condition
# x = 1 
# sum = 0
# while x <= 10:
#     if x % 2 ==0:
#         sum = sum + x
#     x = x + 1
# print(sum) 
# 30   

#the same program for the odd numbers
# x = 1 
# sum = 0
# while x <= 10:
#     if x % 2 != 0:
#         sum = sum + x
#     x = x + 1
# print(sum) 
# 25
  
#break
#you can use break inside a while loop as well
#the program below will stop before it reaches the 5
# x = 0 
# while  x < 15:
#     if x == 5:
#         break
#     print (x)
#     x = x+1
# 0 
# 1
# 2
# 3
# 4

#continue
#to use continue inside a while loop you use the code below
#the program will skip the even numbers as output
# x = 0
# while x <= 10:
#     x = x + 1
#     if x % 2 == 0:
#         continue
#     print(x)
# 1
# 3
# 5
# 7
# 9
# 11    



#FUNCTION
#these tasks have three unique properties
#there are on or more substasks/steps inside
#collectively the have a name
#call the task name to perform the subtasks
#these task are called functions
#it means you are doing some tasks or performing a function

#to declare a function you use the code as below

# def brush_teeth():
#     print("take the tooth brush")
#     print("put the paste on the brush")
#     print("clean teeth")
#     print("wash the toothbrush")
#     print("rinse mouth")
# brush_teeth()   ## call function to execute
# #take the tooth brush
# put the paste on the brush
# clean teeth
# wash the toothbrush
# rinse mouth 

#fuction parameter
#the variable you declared inside the parentheses is called a parameter
#some people call it an argument as well

# def five_times(num):
#     print(num*5)

# five_times(7)
# five_times(13)

# x = 18
# five_times(x)  
# 35
# 65
# 90  

# def add_10(num):
#     result = num + 10
#     print(result)
# add_10(21) 
# 31   

#multiple parameters
#to declare a function with multiple parameters
#just put a coma in between them
#but while calling the function you have to pass
#the same number of parameters

# def add_numbers(first,second):
#     sum = first + second
#     print(sum)
# add_numbers(13,28)
# 41    

#function usage 
#return
#to return a variable or a value or some crazy things from a function
#you use the keyword return before the thing you want to return
#you can set the return from a function to another variable as well
# def add(a,b):
#     return a + b
# sum = add(13,65)
# print(sum)
# 78

#same result with a different program as below
# def add_ex(x,z):
#     sum = x + z
#     print(sum)
# add_ex(13,65)    
# 78

#this was an example but i think there was an error 
#i did a slightly different version that works below
# def get_expense(tuition , rent):
#     total = tuition + rent
#     return total
# get_expense(1000,500)

# def get_expense(tuition,rent):
#     return tuition + rent
# sum = get_expense(1000,500)
# print(sum)

#below is a function that will tell whether a number is odd or not
# def is_odd(num):
#     if num % 2 == 0:
#         print(False)
#     else:
#         print(True)
# is_odd(5)    

#above was an incorrect example in the app
#i modified the returns to print to make it work

# def add(a ,b):
#     return(a + b)
# x = add(2,3)
# y = add(4,5)
# z = add(x,y)
# print(z)
# 14

#you can call a function from another function
# def is_odd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True

# def evenify(num):
#     check_odd = is_odd(num)
#     if check_odd == True:
#         even_num = num * 2
#     else:
#         even_num = num
#     return even_num

# result = evenify(3)
# print  (result)  
# #6

#Factorial
#factorial is a mathematical operation
#it means you need to multiply all the numbers to the number 
#starting by 1 separetly
#5 == 1*2*3*4*5

#when you use a loop inside a function
#it is called iterative function

# def factorial(num):
#     fact = 1
#     while num > 0:
#         fact = fact * num
#         num = num - 1
#     return fact
# print(factorial(4))    
# 24

#recursive function
#this is another way to calculate the factorial of a number
#you call the function from inside of the same function you are declaring

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))  
# 120  

#a function with three parameters that puts them in a list
# def doublified_list(a,b,c):
#     double_nums = [a*2, b*2, c*2]
#     return double_nums
# my_list = doublified_list(4,5,12)
# print(my_list)
# [8, 10, 24]


#loop vs function
#the difference between loop and function is 
#you can call a function from different places
#it can be called with different parameter to use it on different things
#on the other hand a loop is declared in one place
#and does repeating the same task immediately

#default parameter
#you can set a default value to a parameter
#you set a default value by adding an equal sign after the parameter name
#if you dont pass that parameter
#the defaul parameter will be used

# def add(a, b = 5):
#     return a + b

# x = add(2,3)
# print(x)

# y = add(7)
# print(y)

# total = add(x,y)
# print(total)
# 5
# 12
# 17

#keyword arguments
#if you are not sure about the order of the parameters(arguments)
#you can pass arguments by their name 
#and you dont have to maintain their order

# def add(a,b):
#     return a + b

# x = add(a=2,b=3)
# print(x)

# y = add(b=7,a=11)
# print(y)

# total = add(b=x,a=y)
# print(total)
# 5
# 18
# 23

#you can use """ """ right after the function name
#to write the purpose or special notes about a function

#anonymous function
#anonymous function also known as a lambda function 
#is a shortcut way to write a function in one line 
#without giving it a proper name

# double = lambda x:x*2
# print(double(5))
# 10

#acces global variable
#to set a value to a variable not declared inside the function
#or is not a parameter you use the keyword global
#you will get an exception
###there is an error in this example
###i will look into it and come back to correct it
# c = 100
# def add(a,b):
#     c = a + b
#     return c
# x = add(12,23)
# print(x)

# def add(a,b):
#     global c
#     c = a + b
#     return c
# y = add(10,15)
# print(y)
# 35
# 25

#return more than one value
#to return more than one thing from a function 
#you can use a tuple list dictionary class or a dataclass
# def get_a_lot(x):
#     y0 = x + 1
#     y1 = x * 3
#     y2 = y0*y1
#     return (y0,y1,y2)
# things = get_a_lot(5)
# print(things)
# (6, 15, 90)

#variable lenght argument
#in some cases you might not know how many parameters user will pass
#in those cases you can do as the program below
# def add_everything(*x):
#     return sum(x)
# print(add_everything(1,4,5,75,112))
# 197

#main function
# #there is not enough info about this subject
# #i will come back to complete this section
