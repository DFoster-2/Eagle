from tkinter import *
from Apps.Encrypter.Decrypt.EndDecrpt import *
def decrptstart():
  global e
  global e2
  root = Tk()
  root.title("Decrypt")
  root.geometry("720x150")
  label = Label(root, text = "Decrypt")
  label.config(font=('Helvetica bold underline',20))
  label2 = Label(root, text = "Type your encypted mesige here")
  label3 = Label(root, text = "Wright a whole number between 1-25 to be your key")
  e = Entry(root, width = 40, borderwidth = 3)
  e2 = Entry(root, width = 40, borderwidth = 3)
  button_clear = Button (root, text = "clear", bg = "#D9DDDC",padx = 10, pady = 5,command = Clear )
  button_clear2 = Button (root, text = "clear", bg = "#D9DDDC",padx = 10, pady = 5,command = Clear2 )
  submit = Button (root, text = "Submit", bg = "#D9DDDC",padx = 10, pady = 5,command = submit3)
  label4 = Label(root, text = "Click here to submit")
  Button_help = Button (root, text = "Help", bg = "#D9DDDC",padx = 10, pady = 5, command = help,state = DISABLED)
  

  
  label.grid (row =0, column =0)
  label2.grid (row =1, column =0)
  label3.grid (row =2, column =0)
  label4.grid (row =3, column =0)
  e.grid (row = 1, column = 1)
  e2.grid (row = 2, column = 1)
  button_clear.grid (row =1, column =2)
  button_clear2.grid (row =2, column =2)
  submit.grid (row = 3, column = 1)
  Button_help.grid (row =0, column =2)
  
  e .insert(0, "Exmample messige: fdjkgkfrahr#fhgahgh#agjfgaj#")
  e2. insert(0,"4")

def Clear ():
  global e
  e.delete(0,END)

def Clear2 ():
  global e2
  e2.delete(0,END)

def help():
  pass

def submit3():
  global e
  global e2
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  mesige = ""
  code2 = e.get()
  code = code2.upper()
  codesplit = code.split()
  codesplitlenth = len (codesplit)
  key = e2.get()
  keyint = int(key)
  for x in range (0, codesplitlenth):
    temp = codesplit[x]
    lenthoftemp = len(temp)
    for y in range (0, lenthoftemp):
      temp2 = alphabet.find (temp[y])
      if temp2 != -1:
        sum = temp2 - keyint
        if sum < 26:
          temp3 = alphabet[sum]
          mesige = mesige + temp3 
        elif sum > 26:
          temp3 = alphabet[sum - 26]
          mesige = mesige + temp3 
      elif temp2 == -1:
        mesige = mesige + " "
      else:
        print ("somthing rong")
  print ()
  print ("---------------------Start---------------------------------")
  print (mesige)
  print ("---------------------End-----------------------------------")
  print ()
  endScreen2(mesige)
  