##import tkinter as tk
import pickle
from tkinter import *


"""
#### Using this to test pickle
#### I want to save input that is inputted to the Entry widget from tkinter
#### I also want to retrive the saved input later
#### I need to be able to add too the pickle file later
#### END
"""


window = Tk()

window.title("Lexxie Is Sexxie")


window.geometry('850x600')

lbl = Label(window, text="What you wanna save?")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)
txt.focus()

outputBox = Text(window)
outputBox.grid(column=1,row=2)

def clicked():

    res = "Saved the following string --> " + txt.get()
    save = txt.get() + " "
    lbl.configure(text= res)
    f = open('store.pckl', 'wb')
    pickle.dump(save, f)

def load():

    f = open('store.pckl', 'rb')
    readIt = pickle.load(f)
    output = outputBox.insert(END, readIt)

loadBtn = Button(window, text = "Imma load dat shit", command=load)
btn = Button(window, text="Click Me MF", command=clicked)

loadBtn.grid(column=1, row=1)
btn.grid(column=2, row=0)

window.mainloop()
"""
class root(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    
    def create_widgets(self):
        self.label = tk.Label(self)
        self.label
        





if __name__ == "__main__":
    app = root()
    app.mainloop()
"""