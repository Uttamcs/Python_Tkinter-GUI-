from tkinter import *
root= Tk()
root.geometry("655x205")
def getvals():
    print("It Works")
# Heading
Label(root, text="Welcome to IRCTC Rail",font="cambria 15 bold",pady=15).grid(row=0, column=3)
# text for our form
name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
emergency=Label(root, text="Emergency contact")
payment=Label(root, text="Payment mode")

# pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

# tkinter variables for storing entries
nameValue=StringVar
phoneValue=StringVar
genderValue=StringVar
emergencyValue=StringVar
paymentValue=StringVar
foodserviceValue=IntVar

# entries for our form
nameEntry=Entry(root,textvariable=nameValue)
phoneEntry=Entry(root,textvariable=phoneValue)
genderEntry=Entry(root,textvariable=genderValue)
emergencyEntry=Entry(root,textvariable=emergencyValue)
paymentEntry=Entry(root,textvariable=paymentValue)

# packing the entries
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyEntry.grid(row=4, column=3)
paymentEntry.grid(row=5, column=3)

# checkBox and packing it
foodservice=Checkbutton(text="Want to pre-book your meals?",variable=foodserviceValue)
foodservice.grid(row=6, column=3, pady=15)

# Button and assigning it command
Button(text="Submit", command=getvals).grid(row=7,column=3)
root.mainloop()