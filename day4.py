dl = [[1,2,3],[4,5,6],[7,8,9]]
print(dl)

r=int(input("Enter the row number: "))
c=int(input("Enter the col number: "))
print(dl[r][c])


file = open("countries.txt","w")
file.write("India\n")
file.write("USA\n")
file.write("Italy\n")
file.close()

file = open("countries.txt","r")
print(file.read())
file=open("countries.txt","a")
file.write("France\n")
file = open("countries.txt","r")
print(file.read())
file.close()