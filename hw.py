from tkinter import *

window = Tk()

window.title('Getting Started with Widgets')
window.geometry('400x300')

lbl = Label(text="Let's multiply 2 numbers", height=1,
            width=300, fg='white', bg='#072F5F')

n1l = Label(text='First Number', fg='#3895D3')
n1e = Entry()

n2l = Label(text='Second Number', fg='#3895D3')
n2e = Entry()


def display():
    n1 = int(n1e.get())
    n2 = int(n2e.get())
    prod = n1 * n2
    text_box.insert(END, 'Product: ')
    text_box.insert(END, prod)


text_box = Text(height=3)

btn = Button(text='Calculate', command=display, bg='white', fg='black')

lbl.pack()
n1l.pack()
n1e.pack()
n2l.pack()
n2e.pack()
btn.pack()
text_box.pack()

window.mainloop()
