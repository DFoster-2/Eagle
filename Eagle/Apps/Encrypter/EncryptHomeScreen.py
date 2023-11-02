from tkinter import *
from Apps.Encrypter.Encrypt.Encript import *
from Apps.Encrypter.Decrypt.decrypt import *
from Apps.Encrypter.Encrypt.MoreInfo import *
from Apps.Encrypter.Decrypt.MoreInfo2 import *
from Apps.Encrypter.Credits import *
root = Tk()
root.title("Encrypt or Decrypt?")
root.geometry("360x130")

def Encript ():
  Encriptstart()
def Decript():
  decrptstart()
def info_en():
  info()
def info_de():
  info2()
def help():
  credits2()

def encryptstart2(): 
  global root
  label = Label(root, text = "Encrypt or Decrypt")
  label.config(font=('Helvetica bold',20))
  label.grid (row =0, column =0, columnspan = 2)
  
  spaceer = Label(root, text = "..............")
  spaceer2 = Label(root, text = "..............")
  spaceer.grid (row = 4, column = 0)
  spaceer2.grid (row = 4, column = 1)
  
  Button_en = Button (root, text = "Encrypt", bg = "#D9DDDC",padx = 40, pady = 10,command = Encript)
  
  Button_de = Button (root, text = "Decrypt", bg = "#D9DDDC",padx = 40, pady = 10, command = Decript)
  
  Button_en_mi = Button (root, text = "More info", bg = "#D9DDDC",padx = 20, pady = 5, command = info_en)
  
  Button_de_mi = Button (root, text = "More info", bg = "#D9DDDC",padx = 20, pady = 5, command = info_de)
  
  Button_help = Button (root, text = "Credits", bg = "#D9DDDC",padx = 20, pady = 5, command = help)
  
  
  
  
  
  
  Button_help.grid (row =0, column =2)
  Button_en.grid(row = 1, column = 0)
  Button_de.grid(row = 1, column = 1)
  Button_en_mi.grid(row = 2, column = 0)
  Button_de_mi.grid(row = 2, column = 1)
