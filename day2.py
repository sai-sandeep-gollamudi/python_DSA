import random

print(random.randint(1,100))

choice=random.choice(['Apple','Orange','Banana','Pineapple','Mango'])
print(choice)

ui=input("Guess heads or tails, h or t: ")
ch1=random.choice(['h','t'])
if(ch1==ui):
    print("You guessed ir correctly")
else:
    print("Bad luck")

co=0
n=random.choice([1,2,3,4,5])
while(co<2):
    g=int(input("Enter the number between 1 to 5: "))
    if(n==g):
        print("You guessed it correctly")
        co=3
    elif(g>n):
        print("Too high")
    else:
        print("Too low")
    co+=1
