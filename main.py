from tkinter import messagebox
import tkinter as tk
window=tk.Tk()
window.title("Images in tkinter")
window.geometry("200x200")
def show():
    messagebox.showerror("Alert!!!!","virus detectived")
button=tk.Button(window,text="show",command=show)
button.pack()
window.mainloop()