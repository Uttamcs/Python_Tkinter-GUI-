from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("344x377")

    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self, textvar=self.var, relief=RAISED, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print("You clicked me")
    def createButton(self, inptext):
        Button(text=inptext, command=self.click).pack()
    
        
if __name__=='__main__':
    window=GUI()
    window.status()
    window.createButton("mai hu shatakveer")
    window.mainloop()