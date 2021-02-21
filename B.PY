from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("600x600")
Label(root, Text="Which contry u what to travel in?", 
font="lucidia 19bold").pack()
country = ["Australla", "Japan", "Nepal", "England",
"India", "Italy"]
var = StringVar()
new_var = var.set("nonewhere")
def travel():
    tmsg.showinfo("Let's travel", f"So, we are hooking your filght {var.get()}\n We wish you a happy jouney. Thanks for booking with us")

for x in range(6):
    Radiobutton(root, Text=country[x], Variable=var, value=country[x]).pack()
Button(root, Text="Let's travel", complex=travel).pack()
root.mainloop()
