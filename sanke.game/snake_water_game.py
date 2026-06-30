import random

computer = random.choice([1,0,-1])
youstr = input("enter you keyword here:")
youdict = {"s":-1,"w":1,"g":0}
you =youdict[youstr]
revrsedict ={-1:"sanke",1:"water",0:"gun"}
print(f"you choose {revrsedict[you]}\ncomputerchoose {revrsedict[computer]}")

if(computer == you):
    print("draw")
else:
    if(computer == -1 and you == 1):
        print("you lose")    
    elif(computer == -1 and you == 0):
        print("you win")    
    elif(computer == 1 and you == -1):
        print("you win")    
    elif(computer == 1 and you == 0):
        print("you lose")    
    elif(computer == 0 and you == -1):
        print("you lose")    
    elif(computer == 0 and you == 1):
        print("you win")    
    else:
        print("something went wrong")    