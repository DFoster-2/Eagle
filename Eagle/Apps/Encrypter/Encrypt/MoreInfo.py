from tkinter import *
def info():
  root = Tk()
  root.title("More info")
  root.geometry("360x130")
  lable = Label(root, text = "Info")
  lable.config(font=('Helvetica bold underline',20))
  label2 = Label(root, text = "This is the encrypter for Eagle it will incrpt enthing that")
  label3 = Label(root, text = "is just the aferbet or a space for more instructions visit")
  label4 = Label(root, text = "help in Encrypt and for credits go to credits on the apps")
  label5 = Label(root, text = "home screen")
  
  lable.grid (row = 0, column = 0)
  label2.grid (row = 1, column = 0)
  label3.grid (row = 2, column = 0)
  label4.grid (row = 3, column = 0)
  label5.grid (row = 4, column = 0)