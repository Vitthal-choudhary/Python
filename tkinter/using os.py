import tkinter
import os
screen = tkinter.Tk()


def runthis():
    #os.system("
    # file.txt")
    os.system(r"C:\Users\Lenovo\Downloads\jersey.mkv")

button_file = tkinter.Button(text='press me', command=runthis)
button_file.pack()

screen.mainloop()