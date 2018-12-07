import tkinter as tk
from tkinter import ttk

root = tk.Tk()             #Create instance
root.title("Gui Tabs")     #Sets title

tabControl = ttk.Notebook(root)    #Created tabcontrol

tab1 = ttk.Frame(tabControl)       #Create tab and put in tab control
tabControl.add(tab1, text="Tab 1")  #Add the tab
tabControl.pack(expand=1, fill="both");

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")



root.mainloop