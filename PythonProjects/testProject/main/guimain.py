from tkinter import *
from tkinter.messagebox import showinfo
def reply():
    showinfo(title='this is the title',message='Ohhhhh You Clicked the BTN')

window = Tk()
button = Button(window,text='press',command=reply)
button.pack()
window.mainloop()