from tkinter import *
root= Tk()
root.geometry("655x325")
def hello():
    print("Hello Uttam")            
        
f2=Frame(root, bg="grey", borderwidth=5,relief=GROOVE)
f2.pack(side=TOP, fill=X)
l1=Label(f2,text="Table printer", font="Algerian 10 italic")
l1.pack()
f1=Frame(root, borderwidth=6, bg="grey",relief=SUNKEN)
f1.pack(side=LEFT, anchor=NW)
b1=Button(f1, bg="red",fg="black", text="Print Greeting",command=hello,font="cambria 10 italic")
b1.pack(side=LEFT,padx=3)
b2=Button(f1, bg="red",fg="black", text="Print 2 table",font="cambria 10 italic")
b2.pack(side=LEFT,padx=3)
b3=Button(f1, bg="red",fg="black", text="Print now",font="cambria 10 italic")
b3.pack(side=LEFT,padx=3)
b4=Button(f1, bg="red",fg="black", text="Print now",font="cambria 10 italic")
b4.pack(side=LEFT,padx=3)
root.mainloop()