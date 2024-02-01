# This program produces the Fibonacci sequence up to the inputted term (count)

def fibSeq(count):
  nums = [1,1]
  if count > 1:
    count -= 2
    for i in range(count):
      nextVal = nums[i] + nums[i+1]
      nums.append(nextVal)
    
    
    print(*nums, sep=',')
  
  elif count == 1: 
    print("1")
  
  else: 
    print("Invalid number of values")

count = int(input("Enter count: ")) 
fibSeq(count)
