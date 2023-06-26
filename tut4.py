from tkinter import *
Uttam_root=Tk()
Uttam_root.geometry("444x233")
Uttam_root.title("Uttam ka calculator")

# # Important Label Options
# text=adds the text
# bd=background
# fg= foreground
# # font = sets the font
#     1. font=("Algerian", 14, "bold")
#     2. font="Algerian 14 bold"
# padx = x padding 
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label=Label(text= '''
                 Hi, My name is Uttam Kumar \n I'm from patna, Bihar, i'm currently pursuing B.Tech from GLA University,
                 Mathura''', bg="grey", fg="black", padx=104, font="Algerian 14 bold", borderwidth=3, relief= GROOVE)
# # Important Pack Options
# anchor = nw
# side= TOP, BOTTOM, LEFT, RIGHT
# fill
# padx
# pady=
# title_label.pack(anchor=SE)
# title_label.pack(side="bottom", fill=X)
title_label.pack(side="left", fill=Y, padx= 10, pady= 10)

Uttam_root.mainloop()