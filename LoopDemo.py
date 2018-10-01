#Loops are structures used to repeat sections of code.
#They are useful if you have to do the same thing more than once
#or you can establish a pattern. 

# Example 1:
print ("0")
print ("1")
print ("2")
print ("3")
print ("4")
print("***********")
#This is a counted loop. I want you to think about
#count, check, change
# i = 0, 0 < 5, TRUE - RUN LOOP
# i = 1, 1 < 5, TRUE - RUN LOOP
# i = 2, 2 < 5, TRUE - RUN LOOP
# i = 3, 3 < 5, TRUE - RUN LOOP
# i = 4, 4 < 5, TRUE - RUN LOOP
# i = 5, 5 < 5, FALSE - EXIT AND MOVE ON
for i in range (4,12,2,):
	#ANYTHING TABBED IS CONSIDERED THE LOOP BLOCK
	print(i)

print ("***********BACKWARDS***********")
#If you change your increment to go in reverse 
#the check is always i > check, in this case -1    
for i in range (10,-1,-1):
		print (i)

print ("*********** Printing String Characters*****")
str = "Monkey!!!!!!!!!"	
#We can use the loop to go through each index 
#in a string to print out every letter. ALWAYS
#INDICATE THE LENGTH OF A WORD USING THE FUNCTION
#len
for i in range(0, len(str), 1):
	print(str[i])


print("MOVING ON")

print ("***********PRINT STRING IN REVERSE***********")
for i in range (len(str) -1, -1, -1):
	print(str[i])

print("**********PRINT EVERY SECOND LETTER IN STR START AT INDEX 0***********")	
