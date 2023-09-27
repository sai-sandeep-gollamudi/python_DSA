
def get_name():
    u_n = input("Enter your name: ")
    return u_n

def printline(u_n):
    print(f"The name of the user is {u_n}")

def main():
    user_name=get_name()
    printline(user_name)

main()

def get_num():
    num=int(input("Enter the number: "))
    return num

def print_num(num):
    for i in range(1,num+1):
        print(i)

def main():
    num=get_num()
    print_num(num)

main()



import random
def guessing():
    ll=int(input("Enter the starting number of the range: "))
    hl=int(input("Enter the ending number of the range: "))
    comp_num = random.randint(ll,hl)
    return comp_num

def user_interaction():
    print("I am thinking of a number.. ")
    ui = int(input("Can you guess the number I thought?: "))
    return ui

def comparsion(comp_num,ui):
    if(comp_num==ui):
        print("Correct, you win")
    elif(comp_num<ui):
        print("Too high")
        ui=int(input("guess again: "))
        comparsion(comp_num,ui)
    else:
        print("Too low")
        ui = int(input("guess again: "))
        comparsion(comp_num, ui)

def main():
    comp_num = guessing()
    ui=user_interaction()
    comparsion(comp_num,ui)

main()



import random
def addition():
    num1=random.randint(5,20)
    num2=random.randint(5,20)
    print(f"Add these two numbers {num1}, {num2}. Enter your answer in the below line")
    ui=int(input("Answer: "))
    ca=num1+num2
    return(ca,ui)

def subtraction():
    num1=random.randint(25,50)
    num2=random.randint(1,25)
    print(f"Subtract {num2} from {num1}. Enter your answer in the below line")
    ui=int(input("Answer: "))
    ca=num1-num2
    return (ca,ui)

def comparsion(ca,ui):
    if(ca==ui):
        print("Correct")
    else:
        print(f"Incorrect, the answer is {ca}")

def main():
    uc=int(input("1) Addition \n2) Subtraction \nEnter 1 or 2: "))
    if (uc==1):
        ca,ui=addition()
        comparsion(ca,ui)
    elif(uc==2):
        ca,ui=subtraction()
        comparsion(ca,ui)
    else:
        print("Invalid choice.")

main()



import csv

def add():
    user_name=input("Enter your name: ")
    salary=input("Enter your salary: ")
    file = open("Salary.csv","a")
    file.write(user_name+","+salary+"\n")
    file.close()


def view():
    file = open("Salary.csv","r")
    print(file.read())
    file.close()

def main():
    f=1
    while(f==1):
        print("1.Add to the file\n2.View all records\n3.Quit")
        ui=int(input("ENter your choice: "))
        if(ui==1):
            add()
        elif(ui==2):
            view()
        elif(ui==3):
            f=0
        else:
            print("Entered invalid choice.")


main()