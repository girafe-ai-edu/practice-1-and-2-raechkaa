# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
print('Enter integer 4-digit number')

num = int(input())
sum = 0
if (num > 999 and num < 10000):
    digits = [int(i) for i in str(num)]
    #print(digits)
    for i in digits:
        sum += i
    print(sum)