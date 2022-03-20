#Filename: rectangular_prism_exercise.py
#Author: Rongbin Gu
#Date Created: May 11, 2021
#Description: This program calculates the volume and surface
#area of a rectangular prism.

#inputs
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))
h = float(input("Enter the height: "))

#calculations
volume = l * w * h
sa = 2*(w * l + h * l + h * w)

#prints the output
print("The volume is " + str(round(volume, 2)) + " and the surface area is " + str(round(sa, 2)) + ". ")