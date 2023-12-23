from tkinter import *
screen = Tk()
screen.iconbitmap('dobey-deol.ico')
screen.title("Welcome")
screen.geometry("800x400")
screen.config(bg='cyan')

# entries
entry_1 = Entry(screen, bg='white', font=("ALGERIAN", 20))
entry_1.place(x=100, y=100,height=100)


def f():
    print('sairam')
    c = entry_1.get()   # get() helps to get the entry.
    print(c)
    submit_buton["text"] = "hlo"    # [] is se attributes change hojaate h


def disablingfunc(value):
    if value == 1:
        submit_buton['state'] = 'disable'
    elif value == 2:
        submit_buton['state'] = 'active'
    elif value==3:
        entry_1.delete("0","end")   # .delete is used to clear entry box
        

def hide():
    entry_1.config(show="*")    # will show * in place of entered data


submit_buton = Button(screen,text='press', command=f)
submit_buton.pack()
disabling_button = Button(screen,text="Click to disable",command=lambda : disablingfunc(1))
disabling_button.pack()
enabling_buton = Button(screen,text='click to enable', command=lambda : disablingfunc(2))
enabling_buton.pack()
hide_button = Button(screen,text='press to hide', command=hide)
hide_button.pack()
clearbutton = Button(screen,text="press to clear",command=lambda :disablingfunc(3))
clearbutton.place(x=190,y=385)
screen.mainloop()
