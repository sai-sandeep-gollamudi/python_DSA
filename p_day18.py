
# reverse the string with stack
def reverse_string(val):
    s=Stack()
    rs=""
    for c in val:
        s.push(c)
    while not s.is_empty():
        rs+=s.pop()
    return rs


#merge two sorted lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ans=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                ans.next=list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans=ans.next
        while list1 or list2:
            ans.next = list1 if list1 else list2
            if(list1 is not None):
                list1=list1.next
            if(list2 is not None):
                list2=list2.next
            ans = ans.next
        return dummy.next


# checking if there is anything common in between two lists using dictionary
def item_in_common(list1,list2):
    d={}
    for i in list1:
        d[i]=True
    # print(d)
    for i in list2:
        if i in d:
            return True
    return False

#Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
def find_duplicates(list):
    ht={}
    ans=[]
    for i in list:
        if i in ht:
            if i not in ans:
                ans.append(i)
        else:
            ht[i]=True
    return ans


#HT: First Non-Repeating Character
def first_non_repeating_char(s):
    d = {}

    for i in s:
        if i in d:
            d[i] = False
        else:
            d[i] = "First time"

    for i in s:
        if (d[i] is not False):
            return i
    return None

#Group Anagrams
def group_anagrams(list1):
    ht = {}
    for s in list1:
        so=''.join(sorted(s))
        if so in ht:
            ht[so].append(s)
        else:
            ht[so]=[s]
    return list(ht.values())

#Given an array of integers nums and a target integer target,
#find the indices of two numbers in the array that add up to the target.

def two_sum(list1, val):
    t = 0
    ht = {}

    for i in range(len(list1)):
        t = val - list1[i]
        if list1[i] in ht:
            return [ht[list1[i]], i]
        else:

            ht[t] = i
    return []

