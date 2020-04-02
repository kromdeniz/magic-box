# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:44:20 2020

@author: mnm
"""


#exercise 1
#write a program that converts miles to kms using function
#this is my program
# def convert(miles):
#     print(1.6 * miles)
# convert(10)    
# 16

#this is another way to do it
# def convert(miles):
#     return 1.6 * miles
# print(convert(5))
# 8


#Write a program that calculates bmi index using function
#if the bmi is higher than 25 print is overweight
#if the bmi is lower than 25 print is not overweight
# name1 = "mal"
# height_m1 = 2
# weight_kg1 = 90

# name2 = "mal_2"
# height_m2 = 1.8
# weight_kg2 = 70

# name3 = "mal_3"
# height_m3 = 2.5
# weight_kg3 = 160

# def bmi_calculator(name, height_m, weight_kg):
#     bmi = weight_kg / (height_m ** 2)
#     print("bmi: ",bmi)
#     if bmi < 25:
#         return name + " is not overweight"
#     else:
#         return name + " is overweight"

# result1 = bmi_calculator(name1, height_m1, weight_kg1)
# result2 = bmi_calculator(name2, height_m2, weight_kg2)
# result3 = bmi_calculator(name3, height_m3, weight_kg3)
# #bmi:  22.5
# #bmi:  21.604938271604937
# #bmi:  25.6

# print(result1)
# mal is not overweight

# # a simpler one but if you add name variable while defining the function
# #it simply doesnt work
# def bmi_c(height, weight,):
#     bmi = weight /(height ** 2)    
#     print(bmi)
    
# bmi_c(1.9, 100)    
# 27.7    


#exercise
#gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28,
#“Speakers”, 27.00, “Television”, 1000, “Laptop Case”, “Camera Lens”]
#a) Calculate the total price of the all the gadgets.
#b) Calculate the average of all the gadgets.

gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28,“Speakers”, 27.00, “Television”, 1000, “Laptop Case”, “Camera Lens”]