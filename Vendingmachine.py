print("VENDING MACHINE\n") 
stock=70
temp=0
n=int(input("How many pepsi bottles do you need?\n"))
if(n<=stock):
 for i in range(n):
    print("TAKE IT :)")

 print("Have a good drink and enjoy")     
elif(n>=stock):
 temp=n-stock;
 for i in range(temp+1):
  print("Stock is unavailabe\n")
    
print("Unavailable number of stock is",temp)  
print("Sorry for the inconvenince\n")     
