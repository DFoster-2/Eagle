from tkinter import *
def credits2():
  root = Tk()
  root.title("Credits")
  root.geometry("360x130")
  lable = Label(root, text = "Credits")
  lable.config(font=('Helvetica bold underline',20))
  label2 = Label(root, text = "This Eagle macking was done by TeamName132")
  label3 = Label(root, text = "Thanks to stackoverflow for some help")
  
  lable.grid (row = 0, column = 0)
  label2.grid (row = 1, column = 0)
  label3.grid (row = 2, column = 0)
