from tkinter import *


def Clear():
  global username
  username.delete(0, END)


def Clear2():
  global password
  password.delete(0, END)




def submit2():
  global username
  global password
  global root
  from Software.Login.sineIn import SineIn
  Username = username.get()
  Password = password.get()
  root.destroy()
  SineIn(Username, Password)


def rongPaswordusername():
  global root
  global label4
  #label4.config(text = "Rong Username or Pasword")
  print("\033[H\033[J", end="")
  Making_of_loninscreen()

def sine_up():
  root = Tk()
  root.title("sineup")
  root.geometry("400x200")
  root.config(background="#575757")

  label = Label(root, text="Log in ", bg="#575757", fg="#FFFFFF")
  label.config(font=('Helvetica bold underline', 20))
  label2 = Label(root, text="Username", bg="#575757", fg="#FFFFFF")
  label3 = Label(root, text="Password", bg="#575757", fg="#FFFFFF")

  username = Entry(root,
                   width=20,
                   bg="#575757",
                   highlightcolor="red",
                   highlightbackground="#FFFFFF")
  password = Entry(root,
                   width=20,
                   show="*",
                   bg="#575757",
                   highlightcolor="red",
                   highlightbackground="#FFFFFF")

  button_clear = Button(root,
                        text="Clear",
                        bg="#FFFFFF",
                        padx=10,
                        pady=5,
                        command=Clear,
                        highlightbackground="#575757")
  button_clear2 = Button(root,
                         text="Clear",
                         bg="#FFFFFF",
                         padx=10,
                         pady=5,
                         command=Clear2,
                         highlightbackground="#575757")
  submit = Button(root,
                  text="Submit",
                  bg="#FFFFFF",
                  padx=10,
                  pady=5,
                  command= lambda: SineuP(Username, Password),
                  highlightbackground="#575757",
                  highlightcolor="red")


  label4 = Label(root, text="Wating for input", bg="#575757", fg="#FFFFFF")

  label.grid(row=0, column=0, columnspan=3)
  label2.grid(row=1, column=0)
  label3.grid(row=2, column=0)
  username.grid(row=1, column=1)
  password.grid(row=2, column=1)
  button_clear.grid(row=1, column=2)
  button_clear2.grid(row=2, column=2)
  submit.grid(row=3, column=1)
  username.insert(0, "hi")
  password.insert(0, "poo")
  button_sineUp.grid(row=3, column=0)
  label4.grid(row=4, column=1)
def Making_of_loninscreen():
  global username
  global password
  global root
  global label4
  root = Tk()
  root.title("Sine in")
  root.geometry("400x200")
  root.config(background="#575757")

  label = Label(root, text="Log in ", bg="#575757", fg="#FFFFFF")
  label.config(font=('Helvetica bold underline', 20))
  label2 = Label(root, text="Username", bg="#575757", fg="#FFFFFF")
  label3 = Label(root, text="Password", bg="#575757", fg="#FFFFFF")

  username = Entry(root,
                   width=20,
                   bg="#575757",
                   highlightcolor="red",
                   highlightbackground="#FFFFFF")
  password = Entry(root,
                   width=20,
                   show="*",
                   bg="#575757",
                   highlightcolor="red",
                   highlightbackground="#FFFFFF")

  button_clear = Button(root,
                        text="Clear",
                        bg="#FFFFFF",
                        padx=10,
                        pady=5,
                        command=Clear,
                        highlightbackground="#575757")
  button_clear2 = Button(root,
                         text="Clear",
                         bg="#FFFFFF",
                         padx=10,
                         pady=5,
                         command=Clear2,
                         highlightbackground="#575757")
  submit = Button(root,
                  text="Submit",
                  bg="#FFFFFF",
                  padx=10,
                  pady=5,
                  command=submit2,
                  highlightbackground="#575757",
                  highlightcolor="red")

  button_sineUp = Button(root,
                         text="Sine Up",
                         bg="#FFFFFF",
                         padx=10,
                         pady=5,
                         highlightbackground="#575757",command = sine_up)

  label4 = Label(root, text="Wating for input", bg="#575757", fg="#FFFFFF")

  label.grid(row=0, column=0, columnspan=3)
  label2.grid(row=1, column=0)
  label3.grid(row=2, column=0)
  username.grid(row=1, column=1)
  password.grid(row=2, column=1)
  button_clear.grid(row=1, column=2)
  button_clear2.grid(row=2, column=2)
  submit.grid(row=3, column=1)
  username.insert(0, "hi")
  password.insert(0, "poo")
  button_sineUp.grid(row=3, column=0)
  label4.grid(row=4, column=1)
