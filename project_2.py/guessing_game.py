import random
n = random.randint(1,100)
player = -1
computer = n
count = 0
while(player != computer):
    player = int(input("Guess the number :"))
    count += 1
    if(player > computer):
        print("your guessing number is lower try again please")
    else :
        if(player < computer):
            print("your guessing number is higher try again please")   
        elif(player == computer):
            print(f"you have gussed the correct no is {computer} and in these no of attempts {count} :")
            

