#This imports the tkinter "tool box" this contains 
#all the support material to support GUI elements
#by including "as tk" we are giving a short name to use.
#



import tkinter as tk
import math
def submit():


	print("Circumference of a circle")
	r = float(entr.get())
	circumference = 2 * math.pi * r


	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\n The circumference is:"+str(c)+" units squared\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="normal")



root = tk.Tk()
root.title("Circumference of a Circle")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=60, height=15, borderwidth=4, relief=tk.GROOVE)
output.config(state="normal")
output.pack()



root.mainloop()