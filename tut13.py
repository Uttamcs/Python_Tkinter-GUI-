from tkinter import *
import tkinter.messagebox as tmsg
def myfunc():
    print("My func tohh chal rha hai bdhiya ekdm mstt !!!")
def help():
    print("I will help uhh")
    tmsg.showinfo("Help","Uttam Will help you asap!!!")
def rate():
    feedback=tmsg.askquestion("Feedback","Was your experience with this is good?")
    print(feedback)
    if feedback== "yes":
        tmsg.askokcancel("Rate","Rate me on app store")
    else:
        tmsg.showwarning("Warning","Sorry for inconvience caused!! We will contact you soon")
def befriend():
    feedback=tmsg.askretrycancel("Divya kya dostii krogi!!!","Nahi mai nahi krungii")
    if feedback:
        print("Sharm kro!!! Baar baar bolne s koi fayda nahi hai...")
    else:
        print("Achcha kiya dost bhot sahi ho tum :)")
root=Tk()
root.title("Message Box")
root.geometry("655x400")



mainmenu=Menu(root)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
mainmenu.add_cascade(label="File", menu=m1)
root.config(menu=mainmenu)

m2=Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut ", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste",command=myfunc)
m2.add_separator()
m2.add_command(label="Find",command=myfunc)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)


m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="Be friend Divya", command=befriend)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)
root.mainloop()