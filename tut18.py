from tkinter import *
root=Tk()
def upload():
    status.set("Busy...")
    sbar.update()
    import time
    time.sleep(3)
    status.set("Ready Now")
    
root.geometry("655x355")
root.title("Status Bar tutorial")
status=StringVar()
status.set("Ready")
sbar=Label(root, textvariable=status, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="upload", command=upload).pack()

root.mainloop()