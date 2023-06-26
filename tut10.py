from tkinter import *
root=Tk()
root.title("Canvas")
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root, width= canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0, 800,400, fill="red", )
can_widget.create_line(800,0, 0,400, fill="red", )

# To create a rectangle specify parameters in this order => coords 
# of top left corner and coord of bottom right corner
can_widget.create_rectangle(50,30,700,350, fill="light grey")

can_widget.create_text(200,200, text="Python", font="cambria 15 bold")
can_widget.create_oval(5,3,700,350)

root.mainloop() 