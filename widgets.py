from tkinter import *
from datetime import date

window = Tk()
window.title('Greet Screen')
window.geometry('400x300')

lbl = Label(text='Hey There!', height=1, width=300)
name_lbl = Label(text='Your name:', bg='#3895D3')
name_entry = Entry()


def display():
    name = name_entry.get()

    # declaring a global variable to make it accessible anywhere in the program
    global message
    message = "Welcome to the app. \nToday's date is "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text='Begin', command=display, fg='white', bg='#129A10')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()