
#simple input and print
fname = input("Enter your first name: ")
print("The first name of the user is ",fname)

#string
fname2 = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(f"The name of the user is: {fname2+' '+lname}")


#integer calculations
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
print(f"The total is {num1+num2}")

#diner bill
bill = int(input("Enter the total bill: "))
diners = int(input("Number of diners: "))
print(f"Each diner has to pay: {bill/diners}")

#days in hours,minutes
days=int(input("Enter number of days: "))
print(f""" The entered days has {days*24} hours.
      {days*24*60} minutes and {days*24*60*60} seconds
""")


#if statements

int1 = int(input("Enter the number:"))
int2 = int(input("Enter the second number:"))
if(int1>int2):
      print(int2,int1)
else:
      print(int1,int2)



int3 = int(input("Enter the number: "))
if(int3<20):
    print("Thank you.")
else:
    print("Too high")


int4 = int(input("Enter the number between 10 and 20 inclusive: "))
if(int4>=10 and int4<21):
    print("Thank you")
else:
    print("Incorrect answer")


color = (input("Enter your favorite color: "))
if(color == 'RED' or color == 'red' or color =='Red'):
    print("I like red too")
else:
    print(f"I don't like {color}, I like red")


int5 = int(input("Enter the numbers:"))
if(int5==1):
    print("Thank you")
elif(int5==2):
    print("Well done")
elif(int5==3):
    print("Correct")
else:
    print("Error message")



fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
full_name = fname+' '+lname
print(f"The full name is {full_name}")
print(f"The length of the full name is {len(full_name)}")
print(f"In lower case {full_name.lower()}")
print(f"In title case {full_name.title()}")
print(f"In Upper case {full_name.upper()}")


fname2=input("Enter the first name: ")
if(len(fname)<5):
    lname2=input("Enter the last name: ")
    fn=fname2+lname2
    print(f"The full name is {fn.upper()}")
else:
    print(f"the name is {fname2.lower()}")


word = input("Enter the word: ")
c=word[0]
if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
    ans=''
    for i in range(1,len(word)):
        ans=ans+word[i]
    ans=ans+word[0]+'way'
else:
    ans=''
    for i in range(1,len(word)):
        ans=ans+word[i]
    ans=ans+word[0]+'ay'
print(ans)


#for loop

name=input("Enter the name: ")
num=int(input("Enter the number of times you want to repeat it: "))
for _ in range(num):
    print(name)

#each letter on the line

name2=input("Enter the name: ")
num2=int(input("Enter the number of times you want to repeat it: "))
for _ in range(num2):
    for i in range(0,len(name2)):
        print(name2[i])


num3=int(input("Enter the number inbetween 1 and 12: "))
for i in range(1,11):
    print(f"{num3} * {i} = {num3*i}")

total=0
for _ in range(5):
    num=int(input("Enter the number: "))
    c=input("Do you want this number to be added to the total? y or n")
    if(c=='y' or c=='Y'):
        total=total+num
print(total)


choice=input("Which direction to you wnat to go, up or down")
if(choice=='up' or choice=='UP' or choice=='Up'):
    n=int(input("Enter the top number: "))
    i=0
    for i in range(n+1):
        print(i)
        i+=1
elif(choice=='down' or choice=='DOWN' or choice=='Down'):
    n=int(input("Enter the number below 20: "))
    i=n
    for i in range(n):
        print(i)
        i-=1
else:
    print("I don't understand")


#invites
invites=int(input("How many people do you want to invite: "))
if(invites<10):
    for _ in range(invites):
        name=input("Enter the name of the person: ")
        print(f"{name} has been invited")
else:
    print("Too many people")



#while loop

total1=0
while(total1<51):
    n3=int(input("Enter the number: "))
    total1=total1+n3
    print("The total is ",total1)


f=1
while(f==1):
    n4=int(input("Enter the number: "))
    if(n4>5):
        print("The last number you entered was ",n4)
        f=0

var1=int(input("Enter the number: "))
ch='y'
t=var1
while(ch=='y' or ch=='Y'):
    var2=int(input("Enter the number: "))
    t=t+var2
    ch=input("Do you want to add another number? y or n ")
print("The total is ",t)


#party invite
mi='y'
count=0
while(mi=='y' or mi=='Y'):
    name=input("Enter the name of the person you wanted to invite for the party: ")
    print(name,"has been invited")
    count+=1
    mi=input("Do you want to invite more people? y or n ")
print(f"Total people invited to the party is {count}")

#guessing game
compn=50
fl=1
count1=0
while(fl==1):
    g=int(input("Enter the number: "))
    if(g==compn):
        fl=0
        print(f"Well done, you took {count1} attempts")
    else:
        count1+=1
        if(g<compn):
            print("Too low")
        else:
            print("Too high")

