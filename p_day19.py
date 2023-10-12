#remove duplicates from list
def remove_duplicates(li):
    return list(set(li))

#duplicate characters in string
def has_unique_chars(st):
    l=len(st)
    s=set(st)
    ls=len(s)
    if(ls!=l):
        return False
    return True

#find pairs in two lists that match target
def find_pairs(a1,a2,t):
    s=[]
    for i in a1:
        te=t-i
        if te in a2:
            s.append((i,te))
    return s