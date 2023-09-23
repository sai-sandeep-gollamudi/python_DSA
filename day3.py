#Tuples - can't be changed once declared
#Lists - The data in the lists can be changed, and also it can be of different data type
#dictionary - The contents of the dictionary can also be changed, it contains key,value pairs


countries=('India','USA','Italy','France','Spain')
print(f'The country names in the tuple are: {countries}')
i=input("Enter the country name for which you want the index number: ")
print(f"The index for {i} is: {countries.index(i)}")

index=int(input("Enter a number: "))
print(f"The country at the index {index} is {countries[index]}")


#lists
li=['Football','Cricket']
li.append(input("What is your favorite sport: "))
print(f"Sports in the list in sorted order: {sorted(li)}")

#li.sort() - sorts in alphabetical order and saves the list
#sorted(li) - displays the names in sorted order, but doesn't change the order of the orginal list
#both doesn't work if the list has multiple data types



subj = ['English','Maths','Physics','Biology','Chemistry','History']
dl=input("Which subject you don't like: ")
subj.remove(dl)
print(f"The subject in the list are {subj}")


favf={}
i=0
print(("Enter four dishes you like: "))
while(i<4):
   favf[i] = input("dish name: ")
   i+=1

print("Today's menu: ")
for k,v in favf.items():
    print(f"{k} - {v}")

de=int(input("Do you want any item to be removed from menu: "))
del favf[de]
print(sorted(favf.values()))



num=[100,200,300,400]
print("Numbers in the list: ")
for i in num:
    print(i)
un=int(input("Enter the three digit number you want to check: "))
if(un in num):
    print(f"The index of the number {un} is {num.index(un)}")
else:
    print("That number is not present in the list.")



i =0
pi=[]
print("Enter names of the three people you want to invite to the party: ")
while(i<3):
   pi.append(input("Name: "))
   i+=1
co=3
ch=input("Do you want to add another name to the invite list, y or n: ")
while(ch=='y' or ch=='Y'):
    pi.append(input("Name: "))
    co+=1
    ch = input("Do you want to add another name to the invite list, y or n: ")

print(f"{co} are invited to the party")




#arrays

from array import *

nums = array('i',[10,20,30,40,50])
print(nums)

# i - int, l - long int, f - float, d -double

for x in nums:
    print(x)

newvalue=int(input("Enter a number you want to add to nums array: "))
nums.append(newvalue)

nums.reverse()#to reverse the list

nums=sorted(nums) # to sort the array

nums.pop() # pop the last value in the array

new_arr = array('i',[])
it=int(input("How many items you want to add to the array"))
for i in range(it):
    new_arr.append(int(input("Enter the number: ")))
print(new_arr)

print("Attaching it to the nums array")
nums.extend(new_arr)
print("Nums array after adding elements from new_arr")
print(nums)

re=int(input("Enter the element you want to remove: "))
nums.remove(re) #removes the first instance of the element
print(nums)
print(nums.count(10)) #counts how many times the element is present in the array


from array import *
i=0
print("Enter five integers")
arrc=array('i',[])
while(i<5):
    arrc.append(int(input("Number: ")))
    i+=1
arrc=sorted(arrc)

arrc.reverse()

print(arrc)


import random
ranarr=array('i',[])
j=0
while(j<5):
    ranarr.append(random.randint(1,100))
    j+=1
for i in ranarr:
    print(i)

