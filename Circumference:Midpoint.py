import tkinter as tk
from tkinter import ttk
import math

#This imports the tkinter "tool box" this contains 
#all the support material to support GUI elements
#by including "as tk" we are giving a short name to use.



#Main Window
root = tk.Tk() #creates the standard main window.
tabControl = ttk.Notebook(root)    #Created tabcontrol

tab1 = ttk.Frame(tabControl)       #Create tab and put in tab control

tab2 = ttk.Frame(tabControl)       #Create tab and put in tab control

tabControl.add(tab1, text="Tab 1")  #Add the tab

tabControl.add(tab2, text="Tab 2")  #Add the tab

#Three stages to build elements/objects
#1. CONSTRUCT the Object: We build and configure it (OPTIONAL)
#2. Configure the Object: We specify behaviours and settings
#3. Pack the Object: Put it in the window
#Parameters are what we send to the
#ordered parameters: The order we send them to matters. (COMMON)
#named parameters: JavaScript and Python Specific
def fnc1(*args):
	print("Circumference of a circle/Midpoint of a Line")
	r = float(entr1.get()) #takes the value from entr, if there nothing in it
	#or if it is a string you get an error
	c = 2 * math.pi * r
	c = round(c,2)
	output1.config(state="normal")
	outputValue = "Given\nradius:"+str(r)+" units\nThe circumference is:"+str(c)+" units squared\n"
	output1.delete(1.0,tk.END)
	output1.insert(tk.INSERT,outputValue)
	output1.config(state="normal")

def fnc2(*args):


	try:

		entx1.config(background = "white")
		
		entx2.config(background = "white")

		enty1.config(background = "white")

		enty2.config(background = "white")

		x1 = float(entx1.get())

		x2 = float(entx2.get())

		y1 = float(entx1.get())
		y2 = float(entx1.get())
		

		mx = (x1+x2)/2

		mx = round (mx,2)
		my = (y1+y2)/2
		my = round (my,2)

		output1.config(state="normal")
		outputValue = "Given the following points of intersection\nThe midpoint of the line is: "+str(x1)+", "+str(y1)
		output1.insert(tk.INSERT,outputValue)
		output1.config(state="normal")
	except: 
		#Challenge: How do you determine which one is bad input
		entx1.delete(0,tk.END)
		entx1.config(background = "red")
		output1.config(state="normal")
		outputValue = "BAD INPUT"
		output1.insert(tk.INSERT,outputValue)
		output1.config(state="normal")

#***********WIDGET 5,6 (Checkboxes)***********
#How do I track the checkbox state.
var1 = tk.IntVar()
var2 = tk.IntVar()


#What the named parameter does is binds the IntVar to the checkbox.
#If there is a change in the box, there is a change in the variable.

#This is called BINDING

root.title("Circumference of a Circle and Midpoint of a Line")

labr1 = tk.Label(tab1, text="radius")
labr1.pack()

entr1 = tk.Entry(tab1)
entr1.pack()

#This creates the "submit" function 
btn1 = tk.Button(tab1, text="Submit", command=fnc1)
btn1.pack()

output1 = tk.Text(root, width=60, height=15, borderwidth=4, relief=tk.GROOVE)
output1.config(state="normal")


#*************

#Tab 2


labx1 = tk.Label(tab2, text = "x1: ")
labx1.grid(row = 0, column = 0)


entx1 = tk.Entry(tab2)
entx1.grid(row = 0, column = 1)

labx2 = tk.Label(tab2, text = "x2: ")
labx2.grid(row = 0, column = 2)

entx2 = tk.Entry(tab2)
entx2.grid(row = 0, column = 3)

laby1 = tk.Label(tab2, text = "y1: ")
laby1.grid(row = 1, column = 0)

enty1 = tk.Entry(tab2)
enty1.grid(row = 1, column = 1)

laby2 = tk.Label(tab2, text = "y2: ")
laby2.grid(row = 1, column = 2)

enty2 = tk.Entry(tab2)
enty2.grid(row = 1, column = 3)

btn2 = tk.Button(tab2, text="Submit", command=fnc2)
btn2.grid(row=3,column = 2)


tabControl.pack(expand=1, fill="both");
output1.pack()




#print('\nCalculate the midpoint of a line :')

#x1 = float(input('The value of x (the first endpoint) '))
#y1 = float(input('The value of y (the first endpoint) '))

#x2 = float(input('The value of x (the first endpoint) '))
#y2 = float(input('The value of y (the first endpoint) '))

#x_m_point = (x1 + x2)/2
#y_m_point = (y1 + y2)/2
#print();
#print("The midpoint of line is :")
#print( "The midpoint's x value is: ",x_m_point)
#print( "The midpoint's y value is: ",y_m_point)
#print();


#Build the GUI
#Get it running
root.mainloop() #Starts the program.