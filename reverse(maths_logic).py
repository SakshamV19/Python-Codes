number = int(input("Enter the integer number: "))  

rev_num = 0  
  
while (number > 0):  
   
    remainder = number % 10  
    rev_num = (rev_num * 10) + remainder  
    number = number // 10  
  
print("The reverse number is : {}".format(rev_num)) 

 