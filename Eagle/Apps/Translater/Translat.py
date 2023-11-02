import tkinter
from tkinter import *
from translate import Translator



Screen = Tk()
Screen.title("Langage Traslator ")
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
LanguageChoices = {'English','French','German','Spanish',"Chinese"}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('French')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

  
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
Label(Screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)
 

NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
Label(Screen,text="Translated Language").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)
Label(Screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
 
Label(Screen,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)
 

B = Button(Screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)
 
mainloop()