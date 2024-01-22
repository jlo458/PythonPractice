from datetime import date

print("*** e-mail checker ***")
print("A school e-mail address must ...")
print("a) start with four digits for the students intake year")
print("b) contain at least a further two characters")
print("c) end with @lsf.org")
print("d) characters such as @,*,' and a space should not be allowed")
print("e) find the current year to correctly update the range check of possible intake years")

def emailChecker(user): 
  symbols = ["£", "$", "%", "@", "&", "*", " "]
  try: 
    # Checks that the first 4 characters are ints
    yearUser = int(user[:4])

    # Checks that the year given is valid 
    if ((date.today()).year - yearUser) > 7:
      return False

    # Checks that email ends with @lsf.org  
    indexSch = user.find("@lsf.org")
    if indexSch != -1 and indexSch >= 6 and user[indexSch:] == "@lsf.org": 
      # Checks that the chars between year and email signature are not symbols
      return all(char not in symbols for char in user[4:indexSch])
    else: 
      return False 
  except: 
    return False

valid = False
while not valid:
  user = input("Enter Email: ")
  valid = emailChecker(user)  

print("Valid email!")
  
