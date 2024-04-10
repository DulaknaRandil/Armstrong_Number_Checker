#Armstrong numbers are the numbers which are equal to sum of own digits each rasied to the power of  number of digits of it's number

def IsArmstrongNum(num):   #first we create the function for checking if it is an amstrong number
    strNum = str(num)     #convert number to a string
    power = len(strNum)   #get the length of the number get as the power
    total = sum(int(fetchNum) ** power  for fetchNum in strNum)  # by fetchNum get the each number strNum string and raised to the power.
                                                                 #From the sum function get the summation fetchNum's raised to the powers and assign it to total
    return total == num   #check weather total equals to the num 

for num in range(100001):   # Here enter the range you want 
    if(IsArmstrongNum(num)): #check the Amstrong numbers in range
       print(num)           #print them
