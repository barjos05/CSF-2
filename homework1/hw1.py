# Name: Brandon Anderson
# Evergreen Login: andbra16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"
#creates -b
start = -1*(-5.86)
#calculates the data under the square root
underroot= (-5.86)**2-4*1*8.5408
#calculates the addition quadratic
addansw = (start + math.sqrt(underroot))/2*1
#calculates the subtraction quadratic
subansw = (start - math.sqrt(underroot))/2*1
print str(addansw)
print str(subansw)

###
### Problem 2
###

print "Problem 2 solution follows:"
#imports hw1_test and enables me to call the variables by name
from hw1_test import *
print a,b,c,d,e,f

###C:\Users\Anderson
### Problem 3C:\Users\Anderson
###

print "Problem 3 solution follows:"
#uses the imported variables from hw1_test
print ((a and b) or (not c) and not (d or e or f))
# 


###
### Collaboration
###

# Micah, Jason