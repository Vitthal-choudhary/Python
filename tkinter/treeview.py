from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

a = Tk()
a.geometry('800x600')
a = ttk.Treeview(a)
a['columns'] = ('runs', 'balls')


a.mainloop()

 