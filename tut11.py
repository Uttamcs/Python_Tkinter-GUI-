from tkinter import *
def uttam(event):
    print(f"You clicked at {event.x} and {event.y}")
root= Tk()
root.title("Event Handling")
root.geometry("655x355")
widget=Button(root, text="Click me please",bg="grey")
widget.pack()

widget.bind('<Button-1>', uttam)
widget.bind('<Double-1>', quit)
root.mainloop()