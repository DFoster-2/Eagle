from cryptography.fernet import Fernet
def decrypt():
  with open ("Software/Login/key.key","r+") as file:
    key = file.read()
  f = Fernet(key)

  with open ("Software/Login/Paswords.txt","rb") as Td:
    old2= Td.read()
  
  decrypt = f.decrypt(old2)
  
  with open ("Software/Login/Paswords.txt","wb") as TD:
    TD.write(decrypt)