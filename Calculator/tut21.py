from tkinter import *

root = Tk()

# for calculations

def click(event):
    global scValue
    text = event.widget.cget("text")
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(scValue.get())
            except Exception as e:
                print(e)
                value = "Error"
        scValue.set(value)
        screen.update()
    elif text == "C":
        scValue.set("")
        screen.update()
    else:
        scValue.set(scValue.get() + text)
        screen.update()


# GUI frame size
root.geometry("655x764")
# GUI title
root.title("Calculator")
# GUI icon
root.wm_iconbitmap("1.ico")
# GUI background
root.config(bg="light grey")

# Upper frame and label
f1 = Frame(root, bg="light blue", borderwidth=5, relief=RAISED)
Label(f1, text="Apka Apna Calculator", font="algerian 20 bold").pack()
Label(f1, text="-by Uttam ", bg="orange",
      font="lucida 15 italic").pack(side=RIGHT, anchor=SE)

f1.pack(side=TOP, fill=X)

# Entry value
scValue = StringVar()
scValue.set("")
screen = Entry(root, textvar=scValue, font="lucida 40 bold", relief=RAISED)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


# code for button and frame
f2 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
b = Button(f2, text="1", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f2, text="2", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f2, text="3", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f2, text="4", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
f2.pack()

f3 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
b = Button(f3, text="5", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f3, text="6", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f3, text="7", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f3, text="8", padx=15, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
f3.pack()


f4 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
b = Button(f4, text="9", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f4, text="0", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f4, text="/", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f4, text="%", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f4, text=".", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
f4.pack()


f5 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
b = Button(f5, text="C", padx=2, pady=5, bg="red", font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f5, text="+", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f5, text="-", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f5, text="*", padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
b = Button(f5, text="=", bg="light green",padx=2, pady=5, font="cambria 45 bold")
b.pack(side=LEFT, padx=20)
b.bind("<Button-1>", click)
f5.pack()

# code for bottom frame
fl = Frame(root, bg="light blue", borderwidth=5, relief=RAISED)
Label(fl, text="Thanks for using me!!!", font="algerian 20 bold").pack()
fl.pack(side=BOTTOM, fill=X)

root.mainloop()
