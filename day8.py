import sqlite3

with sqlite3.connect("Company.db") as db:
    cursor=db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
id integer PRIMARY KEY,
name text NOT NULL,
dept text NOT NULL,
salary INTEGER
);
""")

cursor.execute("""
Insert into employees values("5","Seth","Sales","90000")
""")
db.commit()

newid = input("Enter id number: ")
newname = input("Enter name: ")
newdept = input("Enter dept name: ")
newsalary = input("Enter salary: ")
cursor.execute("""
insert into employees values(?,?,?,?)
""",(newid,newname,newdept,newsalary))
db.commit()


cursor.execute("select * from employees")
print(cursor.fetchall())

cursor.execute("select * from employees")
for x in cursor.fetchall():
    print(x)

dept_name = input("Enter the dept name you want to view: ")
cursor.execute("select * from employees where dept = ?",[dept_name])
for x in cursor.fetchall():
    print(x)

cursor.execute("select * from employees where salary > 70000")
for x in cursor.fetchall():
    print(x)

cursor.execute("select id,name,salary from employees")
for x in cursor.fetchall():
    print(x)

db.close()

import sqlite3

with sqlite3.connect("pratice.db") as db:
    cursor=db.cursor()

cursor.execute("""
create table if not exists phonebook(
id integer primary key,
First_name text not null,
surname text not null,
phonenumber text
);
""")






print("""
Main menu\n\n
1)View phone book
2)Add to phone book
3)Search for surname
4)Delete person from phone book
5)Quit
""")

uc=int(input("Enter your choice: "))

if(uc==1):
    cursor.execute("select * from phonebook")
    for x in cursor.fetchall():
        print(x)
elif(uc==2):
    newid = input("Enter the id: ")
    newfn = input("Enter the first name: ")
    newln = input("Enter the last name: ")
    newpn = input("Enter the phone number: ")
    cursor.execute("Insert into phonebook values(?,?,?,?)",(newid,newfn,newln,newpn));
    db.commit()
    print("The data has been entered intp phone book\n updated phone book details \n")
    cursor.execute("select * from phonebook")
    for x in cursor.fetchall():
        print(x)
elif(uc==3):
    sn=input("Enter the surname you want to search: ")
    cursor.execute("""
    select * from phonebook where surname=?
    """,[sn])
    for x in cursor.fetchall():
        print(x)
elif(uc==4):
    print("Details in phone book: \n")
    cursor.execute("select * from phonebook")
    for x in cursor.fetchall():
        print(x)
    did=input("Enter the id you want to delete: ")
    cursor.execute("delete from phonebook where id = ?",[did])
    print("The id is deleted\n updated phone book details are: \n")
    cursor.execute("select * from phonebook")
    for x in cursor.fetchall():
        print(x)
elif(uc==5):
    print("Thank you.")
else:
    print("Entered Invalid choice.")