import random
r=random.randint(1,50);
count=0
print("Guess a number between 1 and 50:\n")
while(True):
    count=count+1    
    n=int(input("Guess a number:\n"))
    if(n<r):
        print("The guessed number is low\n") 
    elif(n>r):
        print("The guessed number is high\n")      
    else:
        print("The guessed number is correct\n")
        break

print("The number of guesses is ",count)    