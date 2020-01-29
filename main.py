# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import Progressbar
from tkinter import Menu
from tkinter import ttk
import time
window = Tk()         # Create the application window

# Add a label with the text "Hey"
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)
firstLabel = Label(window, text = "This is a label") 
firstLabel.grid(column=4, row=3)                         
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Click Me")
btn.grid(column=4, row=0)
chk_state = BooleanVar()
 
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=4, row=0)
btn.grid(column=5, row=0)

style = ttk.Style() 
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black') 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar') 
bar['value'] = 70 
bar.grid(column=6, row=1)

menu = Menu(window) 
new_item = Menu(menu) 
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

tk=Tk()
def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 25')
    tk.after(100,clock)
label1=Label(tk,justify='center')
label1.pack()
clock()
window.mainloop()     # Keep the window open
