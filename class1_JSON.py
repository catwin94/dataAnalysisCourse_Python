import json
import pandas as pd

# s = ' {"usuarios": ["mica@mail.co","jerry@gma.com","alber@soup.co"],"contra": ["abc123","caballitos","yoloswag"]}'
# d= json.loads(s)
# email = "mica@mail.co"
# password = "abc123"
# dataFrame = pd.DataFrame(d)

def checkUser(email, password, dataFrame):
  if not(dataFrame[(dataFrame["usuarios"] == email)].empty): 
    if (dataFrame[(dataFrame["usuarios"] == email) & (dataFrame["contra"] == password)].empty):
      print("NO")
    else:
      print("OK")    
  else:
    print("DNE")


## To TEST
# {"usuarios": ["mica@mail.co","jerry@gma.com","alber@soup.co"],"contra": ["abc123","caballitos","yoloswag"]}
# mica@mail.co
# abc123
## RESULT
# NO

usuarios = json.loads(input("Data Frame: "))
dataFrame = pd.DataFrame(usuarios)
email = input("user: ")
password = input("pass: ")
checkUser(email, password, dataFrame)