# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input()
height = input()

#code here
if (float(height) != 0):
    BMI = float(weight)/float(height)**2
    print(round(BMI,3))
else:
    print('Invalid height')