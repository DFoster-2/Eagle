def SineIn(Username,Paswords):
  from Software.Login.Decrypt import decrypt
  decrypt()
  word = Username
  with open("Software/Login/Paswords.txt", 'r') as p:
    lines = p.readlines()
  for line in lines:
    if line.find(word) != -1:
      print(word)
      print(lines.index(line))
      lineU = lines.index(line)
      print(line)
      username = 1
      break
    else:
      print ("no")
      username = 0
  word = Paswords
  for line in lines:
    if line.find(word) != -1:
      print(word)
      print(lines.index(line))
      print(line)
      lineP = lines.index(line)
      pasword = 1
      break
    else:
      print ("no")
      pasword = 0
  from Software.Login.Encrpt import encrypt
  encrypt()
  if username and pasword == 1:
    from Software.HomeScreen import homeScreenStart
    homeScreenStart()
    with open ("Software/Login/Detels.txt","w+") as d:
      temp = str (Username)+"\n"+str (Paswords)
      d.write(temp) 
  else:
    print ("rong pasword or username")
    from Software.Login.Sineinscreen import rongPaswordusername
    rongPaswordusername()