#!/usr/bin/python
# -*- coding: utf-8 -*-


# This program was created for calulation BMI

# The program must show if:

'''

Below the fur
Normal Weigth
OverWeigth
Very Overweigth

'''
from time import sleep
from functions import calc_bmi
import os

# Insert data
print('Please enter the required data\n')
try:
    height = float(input('Enter your height in Meters: '))
    weight = float(input('Enter your weight in Kilo Grams: '))
except ValueError:
    print('Insert a value correct!')
except:
    print('Error unexpected')
sleep(1.5)
os.system('cls')

# Callebed the function
bmi = calc_bmi(weight, height)

# Checking condition of doby
if (bmi >= 18.5) and (bmi <= 24.9):
    print(f'BMI = {bmi}\nYour condition body is normal')
elif bmi >= 25.0 and (bmi <= 29.9):
    print(f'BMI = {bmi}\nYour condition body is OverWeigth')
elif (bmi >= 30.0) and (bmi <= 40.9):
    print(f'BMI = {bmi}\nYou condition doby is Very Overweigth')
elif bmi > 40.9:
    print(f'BMI = {bmi}\nYou condition body is extremely heavy')
elif bmi < 18.5:
    print(f'BMI = {bmi}\nBelow the fur')
else:
    print('Check the past values. Somethings is wrong')