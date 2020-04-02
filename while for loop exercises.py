# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:19:57 2020

@author: mnm
"""


# total = 0
# for i in range(1, 5):
#     total += i
# print(total)



# total2 = 0
# j = 1
# while j < 5:
#     total2 += j
#     j += 1
# print(total2)


# given_list = [5, 4, 4, 3, 1]

# total3 = 0
# i = 0
# while i < len(given_list) and given_list[i] > 0:
#     total3 += given_list[i]
#     i += 1
# print(total3)



# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
# total4 = 0
# for element in given_list2:
#     if element <= 0:
#         break
#     total4 += element
# print(total4)



# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
# total5 = 0
# i = 0
# while True:
#     total5 += given_list2[i]
#     i += 1
#     if given_list2[i] <= 0:
#         break
# print(total5)



#find the sum of the negative numbers 
#using while and for loop

# given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total = 0
# for e in given_list3:
#     if e > 0:
#         continue
#     total += e
# print(total)  
# -17


# given_list3 = [7,5,4,4,3,1,-2,-3,-5,-7]
# total = 0
# e = -1 
# while given_list3[e] < 0:  ###here e represents index of the list
#     total += given_list3[e]
#     e -= 1
# print(total)    
# -17        

# #another way using while loop
# given_list3 = [7,5,4,4,3,1,-2,-3,-5,-7]
# total = 0
# e = len(given_list3) -1 # e represents the last indexed item in the list
# while given_list3[e] < 0:
#     total += given_list3[e]
#     e -= 1
# print(total)
# -17          


#Write a Python program to count the number of even and odd numbers
#from a series of numbers
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# even = 0
# odd = 0
# for e in numbers:
#     if e % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("number of even numbers is :",(even))
# print("number of odd numbers is :",(odd)) 
# number of even numbers is : 4
# number of odd numbers is : 5       

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# count_odd = 0
# count_even = 0
# for x in numbers:
#         if not x % 2:
#     	     count_even+=1
#         else:
#     	     count_odd+=1
# print (count_odd)
# print(count_even)            
             

# Write a Python program that prints all the numbers 
#from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.

#this was my program below this there is a different version
# for x in range(6):
#     if x == 3:
#         continue
#     else:
#         print(x)
# 0
# 1
# 2
# 4
# 5        
        
# #in this version the input is in 1 line 
# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')# this line gives the output in one line
# #print("\n")# this might be optional bc output doesnt change when removed
# 0 1 2 4 5 



#Write a Python program which iterates the integers from 1 to 50. 
#For multiples of three print "Fizz" instead of the number and
#for the multiples of five print "Buzz". For numbers which are multiples of
#both three and five print "FizzBuzz"

# for e in range(1,51):
#     if e % 3 == 0:
#         print("Fizz")
#         continue
#     elif e % 5 == 0:
#         print("Buzz")
#         continue
#     elif e % 5 == 0 and e % 3 == 0:
#         print("fizzbuzz")
#     print(e)    
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz    
# ...        
    
        
#Write a Python program to calculate a dog's age in dog's years.
#Note: For the first two years, a dog year is equal to 10.5 human years. 
#After that, each dog year equals 4 human years.

#my program doesnt work i will come back here later
# human_age = 0
# dog_age = int(input("enter a dogs age to convert it to humans age "))
# if dog_age < 2:
#     dog_age = human_age * 10,5
# else:
#     dog_age = human_age * 4
# print("the dogs age in humans age is" , human_age)    

# h_age = int(input("Input a dog's age in human years: "))

# if h_age < 0:
#  	print("Age must be positive number.")
#  	exit()
# elif h_age <= 2:
#  	d_age = h_age * 10.5
# else:
#  	d_age = 21 + (h_age - 2)*4

# print("The dog's age in dog's years is", d_age)
    


#Write a Python program to convert month name to a number of days
# print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# month_name = input("Input the name of Month: ")

# if month_name == "February":
# 	print("No. of days: 28/29 days")
# elif month_name in ("April", "June", "September", "November"):
# 	print("No. of days: 30 days")
# elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
# 	print("No. of days: 31 day")
# else:
# 	print("Wrong month name") 
    
    
#Write a Python program to display astrological sign for given date of birth  
# day = int(input("Input birthday: "))
# month = input("Input month of birth (e.g. march, july etc): ")
# if month == 'december':
# 	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
# elif month == 'january':
# 	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
# elif month == 'february':
# 	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
# elif month == 'march':
# 	astro_sign = 'Pisces' if (day < 21) else 'aries'
# elif month == 'april':
# 	astro_sign = 'Aries' if (day < 20) else 'taurus'
# elif month == 'may':
# 	astro_sign = 'Taurus' if (day < 21) else 'gemini'
# elif month == 'june':
# 	astro_sign = 'Gemini' if (day < 21) else 'cancer'
# elif month == 'july':
# 	astro_sign = 'Cancer' if (day < 23) else 'leo'
# elif month == 'august':
# 	astro_sign = 'Leo' if (day < 23) else 'virgo'
# elif month == 'september':
# 	astro_sign = 'Virgo' if (day < 23) else 'libra'
# elif month == 'october':
# 	astro_sign = 'Libra' if (day < 23) else 'scorpio'
# elif month == 'november':
# 	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# print("Your Astrological sign is :",astro_sign)
    
  