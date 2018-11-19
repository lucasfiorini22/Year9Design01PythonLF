#First method

import tk as tkinter
import math
def submit():

	print("Circumference of the circle")

	radius = float(input("Enter radius of the circle : "))
 	circumference = 2 * math.pi * radius

	Enter radius of the circle : 5
	Circumference of the circle is : 31.42

#Second Method

def main():
   radius = int(input("circle radius? "))
   pi = 3.14159
   r = radius
   c = 2*pi*r
   print(2*pi*r)
   a = pi*r*r
   print(pi*r*r)
   ratio = c / a
   return(ratio)
   print("the ratio of the circumference to the area is",ratio)

def main():
    
    return c/a

ratio = main()
print(ratio)
# or
print("The ratio is:", ratio)

#Third Method

r = input ("Enter radius of circle")
r = float(r)
a = 3.14*r*r
c = 2*3.14*r
print ("Area =" ,a)
print ("Circumference" , c) 
