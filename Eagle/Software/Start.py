from tkinter import *
from PIL import ImageTk, Image

def boot(root):
  from Software.Login.Sineinscreen import Making_of_loninscreen
  root.destroy()
  Making_of_loninscreen()

root = Tk()

root.geometry("700x500")

frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("default_765x625.png"))

label = Label(frame, image = img)
label.pack()

button = Button (root,  text = "Boot", fg = "white", bg = "black",highlightcolor="black", padx = 700, command = lambda: boot(root)).pack()

root.mainloop()