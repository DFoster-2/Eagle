def SineuP(Username, Password): 
  from Software.Login.Decrypt import decrypt
  decrypt()
  with open("Software/Login/Paswords.txt","r+")as P:
    temp = P.readlines()
    print(temp)
    PandU = temp

  if Username +"\n" in PandU:
    print ("not a valid acount")
  elif Password + "\n" in PandU:
    print ("not a valid acount")
  else:
    print("crating Acount")
    with open("Software/Login/Paswords.txt","r+")as P:
      temp = P.readlines()
    with open("Software/Login/Paswords.txt","w+") as p:
      temp.append(Username)
      temp.append("\n")
      temp.append(Password) 
      temp.append("\n")
      print (temp)
      temp2 = "".join(temp)
      print (temp2)
      
      p.write(temp2)

  from Software.Login.Encrpt import encrypt
  encrypt()
























