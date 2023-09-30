import sqlite3

with sqlite3.connect("Books.db") as db:
    cursor=db.cursor()

cursor.execute("""
create table if not exists bookinfo(
name text primary key,
place_of_birth text not null); 
""")

cursor.execute("""
create table if not exists books(
id integer primary key,
title text not null,
author text not null,
date_published integer not null
);
""")

cursor.execute("""
insert into bookinfo values('Agatha Christie','Torquay'),
('Cecilia Ahern','Dublin'),
('J.K Rowling','Bristol'),
('Oscar Wilde','Dublin')
""")
db.commit()


cursor.execute("""
insert into books values('1','De profundis','Oscar Wilde','1905'),
('2','Harry porter and the chamber of secrets','J.K Rowling','1998'),
('3','Harry porter and the prizoner of Azkaban','J.K Rowling','1999'),
('4','Lyrebird','Cecilia Ahern','2017'),
('5','Murder on the orient express','Agatha Christie','1934'),
('6','Perfect','Cecilia Ahern','2017'),
('7','The marble collector','Cecilia Ahern','2016'),
('8','The murder on the links','Agatha Christie','1923'),
('9','The picture of dorian grey','Oscar Wilde','1890')
""")
db.commit()

print("Displaying authors data: ")

cursor.execute("Select * from bookinfo")
for x in cursor.fetchall():
    print(x)

print("To find the authors and their works based on place of birth")
us =str(input("please enter a place you want to search: "))

print(f"The works of authors born in {us} are : ")
cursor.execute("""
Select title,date_published,author from books where author in (select name from bookinfo where place_of_birth = ?)
""",[us])
for x in cursor.fetchall():
    print(x)

uy = int(input("To get all the books published after the given year, enter the year: "))
print(f"Books published after {uy}: ")
cursor.execute("""
select * from books where date_published > ? order by date_published
""",[uy])
for x in cursor.fetchall():
    print(x)
db.close()

