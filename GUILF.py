#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements.
#By including "as tk" we are giving a short name to use.
import tkinter as tk


#Main Window
root = tk.Tk() #creates the standard main window.


#Three stages to build elements/objects
#1. CONSTRUCT the Object: We build and configure it (OPTIONAL)
#2. Configure the Object: We specify behaviours and settings
#3. Pack the Object: Put it in the window
output = tk.Text(root, height = 10, width = 30) #Parameters are what we send to the
#ordered parameters: The order we sned them to matters. (COMMON)
#named parameters: JavaScript and Python Specific
output.config(state = "disable", background = "blue")
output.grid(row = 0, column = 0, rowspan = 5)


#**************WIDGET 2,3,4 (LABELS)*************
labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0,

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0,

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0,

#***********WIDGET 5,6 (Checkboxes)***********
#How do I track the checkbox state.
var1 = IntVar()
var2 = IntVar()

#What the named parameter does is binds the IntVar to the checkbox.
#If there is a change in the box, there is a change in the variable.
#This is called BINDING

cHC = tk.CHeckbutton(root, text="Expand", variabl=var)
cHC = grid(row = 0, column = 1)

#We are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the prgram.