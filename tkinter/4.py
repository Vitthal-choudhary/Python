from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

screen = Tk()
screen.geometry("800x600")
screen.config(bg="green")
screen.title("menu")
screen.iconbitmap("dobey-deol.ico")
# option menu
listofitems = ["dosa","idli","coffee"]
menuVar = StringVar()
menu = OptionMenu(screen,menuVar,"menu : ",listofitems)    # here no star so it look bad
menu.pack()
menu = ttk.OptionMenu(screen,menuVar,"menu : ",*listofitems)    # * makes it look in list form only
menu.pack()
# ttk ki looks
buttonfromttk = ttk.Button(screen,text="this stylish button is from ttk")   # this button is stylish
buttonfromttk.pack()


# tree view
screen = ttk.Treeview(screen)
screen['columns'] = ('runs', 'balls')   # #0 column is always there.
screen.heading("#0",text='Name',anchor='n')  # anchor must be n, ne, e, se, s, sw, w, nw, or center.
screen.heading("runs",text="runs")
screen.heading("balls",text="Balls")
screen.place(x=200, y=150)
screen.mainloop()

