from tkinter import *
root=Tk()
root.geometry("654x451")
root.title("Tips and tricks tutorial")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

# For changing background
root.config(background="grey")
print(f"{width}x{height}")

Button(root, text="Close", command=root.destroy).pack()
root.mainloop()