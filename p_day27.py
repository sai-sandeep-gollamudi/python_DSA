def merge_sort(li):
    if(len(li)==1):
        return li
    mid_ind = int(len(li)/2)
    left=merge_sort(li[:mid_ind])
    right=merge_sort(li[mid_ind:])

    return merge(left,right)

def merge(list1,list2):
    i=0
    j=0
    res = []
    while(i<len(list1) and j<len(list2)):
        if(list1[i]>list2[j]):
            res.append(list2[j])
            j+=1
        else:
            res.append(list1[i])
            i+=1
    while(i<len(list1)):
        res.append(list1[i])
        i+=1
    while(j<len(list2)):
        res.append(list2[j])
        j+=1
    return res


l = [7,8,2,4,6,1,9]
print(merge_sort(l))
