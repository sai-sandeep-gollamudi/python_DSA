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

def delete():
    file=open("Salary.csv","r")
    tmp=[]
    for r in file:
        tmp.append(r)
    file.close()
    x=0
    for i in tmp:
        print(f"{x} - {i}")
        x+=1
    rn=int(input("Enter the row number you want to delete: "))
    del tmp[rn]
    file = open("Salary.csv","w")
    for r in tmp:
        file.write(r)
    file.close()

def main():
    f=1
    while(f==1):
        print("1.Add to the file\n2.View all records\n3.Delete a record\n4Quit")
        ui=int(input("Enter your choice: "))
        if(ui==1):
            add()
        elif(ui==2):
            view()
        elif(ui==3):
            delete()
        elif(ui==4):
            f=0
        else:
            print("Entered invalid choice.")


main()