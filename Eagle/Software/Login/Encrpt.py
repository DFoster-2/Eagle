from cryptography.fernet import Fernet

def MakeKey(): 
  with open ("Software/Login/key.key","wb") as file:
    file.write (Fernet.generate_key())
def encrypt():

  with open ("Software/Login/key.key", "r+") as keyFill:
    key = keyFill.read()
  
  with open ("Software/Login/key.key", "rb") as keyFill:
    key = keyFill.read()
  
  f = Fernet(key)
  
  with open ("Software/Login/Paswords.txt","rb") as T:
    old = T.read()
  
  encrypt = f.encrypt(old)
  
  with open ("Software/Login/Paswords.txt","wb") as TC:
    TC.write(encrypt)
  