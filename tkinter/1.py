from tkinter import *
"""will import everything and make it part of our local name space.
 if i do import tkinter then i will have to do tkinter.Tk()"""
from PIL import Image,ImageTk
screen = Tk()   # Tk is a class in tkinter
#screen.iconbitmap('dobey-deol.ico')
screen.title("Welcome")
screen.geometry("800x400")
screen.config(bg='yellow')
#screen.minsize(800, 600)    can restrict size of screen.
#screen.maxsize(1000, 800) .

labelwidgeet = Label(screen, text="hello", bg='red',fg='black')
labelwidgeet.place(x=10,y=50)   # will make small white portion with hello written
# place, pack, grid are geometry managers.
#labelwidgeet1 = Label(screen, text="hello", bg='red',fg='black')
#labelwidgeet.pack()
'''labelwidgeet2 = Label(screen, text="hello", bg='red',fg='black')
labelwidgeet2.grid()''' # bcoz we can't use all at same time.


def press_button():
    print('sairam')
    #labelwidgeet1 = Label(screen, text="hello", bg='red', fg='black')
    #labelwidgeet1.pack()
    another_screen = Toplevel(screen)   # will open new screen when button pressed. Tk() will also do same but small screen will not close if main is closed.
    another_screen.mainloop()

button_var = Button(screen,text='touch me',command=press_button)
button_var.place(x=60,y=60)

image_var = Image.open('dobey-deol.ico')
image_var = ImageTk.PhotoImage(image_var.resize((50,50)))
image_button = Button(screen,image=image_var)
image_button.place(x=50,y=10)
screen.mainloop()