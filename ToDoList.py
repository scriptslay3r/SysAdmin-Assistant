from tkinter import *


window = Tk()

window.title("")


window.geometry('1000x600')

lbl = Label(window, text="What you wanna save?")

lbl.grid(column=0, row=0)

txt = Entry(window,width=30)

txt.grid(column=1, row=0)
txt.focus()

outputBox = Text(window)
outputBox.grid(column=1,row=2)

def clicked():
    todoArray = ["Your ToDo List"]
    res = "Saved the following string --> " + txt.get()
    save = txt.get() + "\n"
    lbl.configure(text= res)
    toDoList = open('incomplete.txt','a')
    toDoList.write(save)
    toDoList.close()
    txt.delete(0, 'end')

def load():

    outputBox.delete('1.0', 'end')
    toDoList = open('incomplete.txt', 'r')
  
    output = outputBox.insert(END, toDoList.read())
    clearBtn.grid(column=1, row=3)

def clear():
    #clearedList = open('incomplete.txt', 'w+')
    #completedList = open('completed.txt', 'w+')
    with open('incomplete.txt') as f:
        with open('completed.txt', 'a') as f1:
            for line in f:
                f1.write(line)
    clearedList = open('incomplete.txt', 'w+')
    clearedList.write("")
    outputBox.delete('1.0', 'end')


def showCompleted():
    outputBox.delete('1.0', 'end')
    with open('completed.txt', 'r') as f:
        for line in f:
            outputBox.insert(END, line)
    open('completed.txt', 'r').close()
    clearBtn.grid_forget()


loadBtn = Button(window, text = "Imma load dat shit", command=load)
btn = Button(window, text="Click Me MF", command=clicked)
clearBtn = Button(window, text="Clear Saved List", command=clear)
completedBtn = Button(window, text="Show My Completed List", command=showCompleted)

loadBtn.grid(column=1, row=1)
btn.grid(column=2, row=0)
clearBtn.grid(column=1, row=3)
completedBtn.grid(column=2, row=3)
window.mainloop()