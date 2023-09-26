
file = open("Numbers.txt","w")
file.write("1, ")
file.write("2, 3, 4, 5, ")
file.write("6, ")
file.write("7, ")
file.close()

file = open("Names.txt","w")
file.write("John\n")
file.write("Rebecca\n")
file.write("Smith\n")
file.write("Vanessa\n")
file.write("Jack\n")
file.close()

file = open("Names.txt","r")
print(file.read())

file = open("Names.txt","a")
n = input("Enter a name: ")
n=n+'\n'
file.write(n)
file.close()
file=open("Names.txt","r")
print(file.read())


print('''
#1) Create a new file
#2)Display the file
#3) Add a new item to the file
''')
ch=int(input("Enter the choice: "))
if(ch==1):
    file=open("Subject.txt","w")
    subj=input("Enter the school subject: ")
    file.write(subj)
    file.write("\n")
    file.close()
elif(ch==2):
    file=open("Subject.txt","r")
    print(file.read())
    file.close()
elif(ch==3):
    file=open("SUbject.txt","a")
    ap=input("Enter the subject: ")
    file.write(ap)
    file.write("\n")
    file.close()
    file=open("Sunject.txt","r")
    print(file.read())
    file.close()
else:
    print("Entered invalid number")


print("Names in the 'Names.txt' file: ")
file = open("Names.txt","r")
print(file.read())
file.close()
invn = input("Enter the name you don't want to save in the next fie: ")
invn=invn+'\n'

file = open("Names.txt","r")
for r in file:
    if r!=invn:
        file=open("Names2.txt","a")
        file.write(r)
        file.close()
file.close()

file = open("Names2.txt","r")
print(file.read())


#Reading and writting to a csv file
# modes available
# w - creates a new file and write in it, if the file already exists, overwrites on it, deleting previous data
# x - created a new file and writes in it, if the file already exists, program gets crashed instead of overwriting it
# r - reads the csv file
# a - opens for writing, and appends the data to the end of file


import csv

file = open("stars.csv","w")
rec = 'Jack,26,leo\n'
file.write(str(rec))
file.close()

file=open("stars.csv","a")
na = input("Enter name: ")
age = input("Enter age: ")
ss = input("Enter star sign: ")
newr= na+","+age+","+ss+"\n"
file.write(str(newr))
file.close()

file = open("stars.csv","r")
for r in file:
    print(r)
file.close()

file = open("stars.csv","r")
reader = csv.reader(file)
s=input("Enter the term you want to search: ")
for r in file:
    if s in str(r):
        print(r)

file = open("Books.csv","w")
file.write("To kill a mockingbird, Harper Lee, 1960\n")
nl="A brief history of time, Stephen Hawking, 1988\n"
file.write(str(nl))
nl="The great gatsby, F.Scott Fitzgerald , 1922\n"
file.write(str(nl))
nl="The man who mistook is wife for hat, Oliver sacks, 1985\n"
file.write(str(nl))
nl="Pride and prejudice, Jane Austen, 1813\n"
file.write(str(nl))
file.close()

file=open("Books.csv","r")
print(file.read())


rc=int(input("Enter how many records you want to add to the file: "))
file=open("Books.csv","a")
for i in range(rc):
    nn=input("Enter the novel name: ")
    an=input("Enter the author name: ")
    year=input("Enter the year the book was published: ")
    nr=nn+", "+an+", "+year+"\n"
    file.write(nr)
file.close()

s=input("Enter the author name you want to search: ")
file=open("Books.csv","r")
c=0
for r in file:
    if s in r:
        print(r)
        print("\n")
        c+=1
if(c==0):
    print("No books with the author is present in the 'Books' file.")


sy = int(input("Enter the starting year: "))
ey = int(input("Enter the ending year: "))

file = list(csv.reader(open("Books.csv","r")))
tmp=[]
for r in file:
    tmp.append(r)

l=0
for r in tmp:
    if(int(tmp[l][2])>=sy and int(tmp[l][2])<=ey):
        print(r)
        l+=1


temp=[]
file = list(csv.reader(open("Books.csv","r")))
for r in file:
     temp.append[r]

print("The data in the file is: \n")
for i in range(len(temp)):
    print(temp[i])

rd=int(input("Enter the row number which you eant to delete: "))
del temp[rd]
