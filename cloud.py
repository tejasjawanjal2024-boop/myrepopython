from tkinter import Label, Tk
import time

root = Tk()
root.title("Clock")
root.geometry("220x80")
root.resizable(False, False)

label = Label(root, font=("Arial", 28), bg="black", fg="lime")
label.pack(anchor="center", fill="both", expand=True)


def tick():
    label.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, tick)


tick()
root.mainloop()
