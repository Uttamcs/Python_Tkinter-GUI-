from tkinter import *
import tkinter.messagebox as tmsg
root =Tk()
root.geometry("655x455")
root.title("Radio Button tutorial")
def order():
    tmsg.showinfo("Order Recieved",f"We have recieved {var.get()} order. Thanks for ordering")

var=StringVar()
var.set("Dosa")
f1=Frame(root,bg="grey", borderwidth=5, relief="raised" )
Label(f1, text="What would you like to have Sir/Madam?", font="Lucida 20 italic").pack()
f1.pack(side=TOP, fill=X)

radio=Radiobutton(root, text="Dosa", padx=10, variable=var,value="Dosa").pack(anchor=W)
radio=Radiobutton(root, text="Idly", padx=10, variable=var,value="Idly").pack(anchor=W)
radio=Radiobutton(root, text="Samosa", padx=10, variable=var,value="Samosa").pack(anchor=W)
radio=Radiobutton(root, text="Chowmin", padx=10, variable=var,value="Chowmin").pack(anchor=W)
radio=Radiobutton(root, text="Veg-Roll", padx=10, variable=var,value="Veg-Roll").pack(anchor=W)
radio=Radiobutton(root, text="Egg-Roll", padx=10, variable=var,value="Egg-Roll").pack(anchor=W)

Button(root, text="Order Now", command=order).pack()
root.mainloop()
