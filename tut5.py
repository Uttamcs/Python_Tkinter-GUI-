from tkinter import *
root= Tk()
root.title("Pycharm_Interface_by_Uttam")
root.geometry("655x325")
f1=Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root, bg="grey", borderwidth=9, relief=GROOVE)
f2.pack(side=TOP, fill=X)
l1=Label(f1,text="Project_by_Uttam", font="cambria 13 italic")
l1.pack()
l2=Label(f2,text="Welcome to PyCharm", font="cambria 20 bold",fg="green")
l2.pack()
f3=Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
f3.pack(side=BOTTOM, fill=X)
l3=Label(f3, text="Thanks for using PyCharm", font="Algerian 10 italic")
l3.pack()
root.mainloop()