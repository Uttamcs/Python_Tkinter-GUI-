from tkinter import *
root=Tk()
root.title("Window Resizer")
root.geometry("285x135")
Label(root, text="Window Resizer", font="algerian 15 bold", bg="red").grid(column=1)
def update():
    print("Updating the GUI")
    root.geometry(f"{width.get()}x{height.get()}")
width=StringVar()
height=StringVar()
Label(root, text="Width:", font="cambria 15 italic").grid(row=1,column=0)
Label(root, text="Height:", font="cambria 15 italic").grid(row=2,column=0)

Entry(root, textvariable=width).grid(row=1, column=1)
Entry(root, textvariable=height).grid(row=2, column=1)
Button(root,text="Apply", command=update).grid(row=3, column=1)


root.mainloop()