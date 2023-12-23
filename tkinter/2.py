from tkinter import *

screen = Tk()
screen.iconbitmap('dobey-deol.ico')
screen.title("Learning !! ")
screen.geometry("800x600")
screen.config(bg="cyan")

# Radio Buttons
Radio_anything = IntVar()


def press_button():
    print(Radio_anything.get())


# Label frame
frame_var = LabelFrame(screen,text="title",width=100,height=100)
frame_var.place(x=50,y=50)
button1 = Radiobutton(frame_var, text='sai', variable=Radio_anything, value=1)
button1.pack()
button2 = Radiobutton(frame_var,text='ram', variable=Radio_anything, value=2)
button2.pack()
pressbutton = Button(frame_var,text='press', command=press_button, padx=10,pady=10)
pressbutton.pack()

# canvas
canvas_var = Canvas(screen,bg='pink',width=200,height=200)
line = canvas_var.create_line(0,0,100,100,200,200,10,50)  # will keep joining points
rect = canvas_var.create_rectangle(70,70,150,150)
oval = canvas_var.create_oval(0,0,100,100)
canvas_var.pack()

list_var = Listbox(screen,selectmode='multiple')
list_var.pack()
button_for_listbox = Button(screen,text='press for list')
button_for_listbox.pack()

screen.mainloop()
