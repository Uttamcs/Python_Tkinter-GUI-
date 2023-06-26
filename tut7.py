from tkinter import *
def getvals():
    print(f"The value of username is {userValue.get()}")
    print(f"The value of password is {passValue.get()}")
root= Tk()
root.geometry("655x305")
user=Label(root, text="Username")
password=Label(root, text="Password")
user.grid()
password.grid(row=1)
# types of var in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar
userValue=StringVar()
passValue=StringVar()

userEntry =Entry(root, textvariable=userValue)
passEntry =Entry(root, textvariable=passValue)
userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()
root.mainloop()