
#bubble sort code
def bubble_sort(input):
    for i in range(len(input)-1,0,-1):
        for j in range(i):
            if(input[j]>input[j+1]):
                temp = input[j]
                input[j] = input[j+1]
                input[j+1] = temp
    return input


def selection_sort(input):
    for i in range(len(input)-1):
        min_index=i
        for j in range(i+1,len(input)):
            if(input[min_index]>input[j]):
                min_index=j
        temp=input[min_index]
        input[min_index] = input[i]
        input[i] = temp
    return input

def insertion_sort(input):
    for i in range(1,len(input)):
        ind = i
        for j in range(i,0,-1):
            if(input[ind]>input[j]):
                ind=j
                temp = input[ind]
                input[ind] = input[j]
                input[j] = temp
    return input

i = [5,3,1,7,4,8,6,9,2]
print(bubble_sort(i))
print(selection_sort(i))
print(insertion_sort(i))




