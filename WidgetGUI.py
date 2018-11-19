import tkinter as tk

root = tk.Tk() #creates the standard main window.

output = tk.Text(root, height = 10, width = 30)

output.config(state = "disable", background = "blue")
output.grid(row = 0, column = 0, rowspan = 5)

#**************WIDGET 2,3,4 (LABELS)*************

labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0,

labInput2 = tk.Label(root, text = "Input 2")
labInput2grid(row = 6, column = 0,

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0,


#***********WIDGET 5,6 (Checkboxes)***********

var1 = IntVar()
var2 = IntVar()

cHC = tk.CHeckbutton(root, text="Expand", variabl=var)
cHC = grid(row = 0, column = 1)

root.mainloop() #Starts the program.