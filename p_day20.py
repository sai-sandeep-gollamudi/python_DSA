#finding lonquest sequence in list

def longest_consecutive_sequence(li):
    s= set(li)
    c=0
    ans=0
    for i in li:
        if i-1 not in s:
            temp=i
            c=1
            while(temp+1 in s):
                c+=1
                temp+=1
            ans = max(ans,c)
    return ans