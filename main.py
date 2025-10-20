# Code was wrong.
# SOURCE: https://www.youtube.com/watch?v=olom5Ow7zbo
from tkinter import * # Imports te TKinter libraty

root = MyArtGallery()
# substites 'root = TK()'
root.title("My Art Gallery")
root.geometry("600x800")

def ClickButton():
    if len(inputField.get()) == 0:
        labelOne["text"] = "Please enter your name."
    else:
        labelOne["text"] = "Hello" + inputField.get()

inputField = Entry(root, width=60, font=("Comic Sans, 24"), bg="royalblue", fg="midnightblue", justify="center")
buttonOne = Button(root, text="ClickMe", padx=50, pady=5, command=ClickButton, bg="gold", font=("Comic Sans, 15"))
labelOne = Label(root, text="?????", font=("Comic Sans, 15"), fg="purple", pady=20)

inputField.pack(pady=20)
buttonOne.pack(pady=10)
labelOne.pack()

root.mainloop()
