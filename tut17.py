from tkinter import *
root=Tk()
root.geometry("655x455")
root.title("Scroll bar tutorial")

# For connecting y scrollbar to a widget 
# 1. widget (yscrollcommand=scrollbar.set)
# 2. scrollbar. config(command=widget.yview)

scrollbar1=Scrollbar(root)
scrollbar2=Scrollbar(root, orient=HORIZONTAL)
scrollbar1.pack(side=RIGHT,fill=Y)
scrollbar2.pack(side=BOTTOM,fill=X)
listBox=Listbox(root, yscrollcommand=scrollbar1.set, xscrollcommand=scrollbar2.set)
for i in range(255):
    listBox.insert(END, f"string{i}")
listBox.pack(fill=BOTH)
scrollbar1.config(command=listBox.yview)
scrollbar2.config(command=listBox.xview)
root.mainloop()