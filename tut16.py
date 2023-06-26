from tkinter import *
root =Tk()
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
root.geometry("655x455")
root.title("ListBox")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END, "We have added a new text")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
