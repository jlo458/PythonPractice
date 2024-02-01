# This program opens an existing file "scores.txt" and adds three sets of fixtures (school, no. Goals) 
# Must have "scores.txt" file available 
# Functionality is a bit useless & can be improved, but shows ability to use files & exception handling

def menu(): 
  print("a: Enter new data")
  print("b: Load and display data")
  print("c: Quit")

def writeFile(fN):
  file = open(fN, "a")
  list = [[],[]]
  for _ in range(3): 
    errorCheck = True
    while errorCheck:
      inputs = (input("Enter school and no. goals: ")).split()
      try: 
        if int(inputs[1]) >= 0 and int(inputs[1]) <= 20:
          list[0].append(inputs[0])
          list[1].append(inputs[1])
          errorCheck = False
    
      except: 
        pass

  str = ''
  for i,j in zip(list[0], list[1]): 
    str += (i + ' ' + j + ',') 
    file.write(str) 
  file.write("\n")

def readFile(fN):
  file = open(fN, "r")
  print(file.read())
  file = file.close()


fileName = "scores.txt"

active = True
while active:
  menu()  
  opt = input("Enter Function: ")
  if opt == "a": 
    writeFile(fileName) 

  elif opt == "b": 
    readFile(fileName)

  elif opt == "c": 
    active = False
    
  
