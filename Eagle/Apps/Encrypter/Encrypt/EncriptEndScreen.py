from tkinter import *
import pyperclip
def endScreen(mesige):
  root = Tk()
  root.title("Mesige")
  #root.geometry("350x200")
  
  label = Label(root, text = "Your Encrypted mesige")
  label.config(font=('Helvetica bold underline',20))
  label.pack()
  
  Outcum = Label(root, text = "Your Mesige is ")
  Outcum.config(font=('Helvetica bold underline',10))
  Outcum.pack()
  
  Outcum2 = Label(root, text = mesige)
  Outcum2.config(font=('Helvetica bold underline',15))
  Outcum2.pack()
  

  
  #label.grid (row =0, column =0)
  #Outcum.grid (row =1, column =0)
  #Outcum2.grid (row =2, column =0)

  togmail = Button (root, text = "Mesiges", command = lambda: addToClipBoard(mesige), state = DISABLED).pack()
  togemail = Button (root, text = "Gmail", command = lambda: addToClipBoard(mesige), state = DISABLED).pack()
  
  #togmail.grid (row =3, column =0)
  
  #togemail.grid (row =4, column =0)


def addToClipBoard (mesige):
  pass 