from tkinter import *
import tkinter.messagebox as tmsg
root =Tk()
root.geometry("355x455")
root.title("Slider tutorial")
def getdollar():
    print(f"We have credited {myslider.get()} dollars in your bank account")
    tmsg.askokcancel("Amount credited!!",f"We have credited {myslider.get()} dollars in your bank account")
Label(root, text="How many dollars you want?").pack()
myslider= Scale(root, from_=0, to_=100 , orient=HORIZONTAL, tickinterval=5)
myslider.set(41)
myslider.pack(side=TOP, fill=X, pady=15, padx=15)

Button(root, text="Get Dollars", pady= 10, command=getdollar).pack()
root.mainloop()
