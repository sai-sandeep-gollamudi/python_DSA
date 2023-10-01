class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
        self.length+=1
    def pop(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            temp=self.head
            self.head=None
            self.tail=None
        else:
            pre=self.head
            temp=self.head
            while(temp.next is not None):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
        self.length-=1
        return temp.value

    def prepend(self,value): #add node to the start of the list
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True #optional just in case you're using this method in other method

    def pop_first(self):
        if(self.length==0): #no nodes in the list
            return None
        elif(self.length==1): #one node in the list
            temp=self.head
            self.head=None
            self.tail=None
        else: #multiple nodes in the list
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length-=1
        return temp.value

    def get(self,index):
        if(index<0 and index>self.length):
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp

    def set_value(self,index,value):
        temp=self.get(index) #calling another method in this metod, get returns the address of the node at index
        if temp: #if temp returns  a value that node exists
            temp.value=value #changing the value of that node
            return True
        return False # if that node doesn't exist, returns false

    def insert(self,index,value):
        if(index<0 or index>self.length):
            return False #return false if the index doesn't exist less than zero or greater than length
        if(index==0):
            return self.prepend(value) #if index is zero, using already existing mehod to insert the value
        if(index==self.length-1):
            return append(value) #if the index is equal to length-1, using append to insert value at the end
        new_node=Node(value) #if above conditions don't match, creating a new node
        temp=self.get(index-1) #get previous node of the index
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    def remove(self,index,value):
        if(index<0 or index>=self.length):
            return None
        if(index==0):
            return self.pop_first()
        if(index==self.length-1):
            return pop()
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after



ll = LinkedList(5)
ll.append(7)
ll.append(9)
ll.append(11)


##############################################################################

#leet code problems
#Methid for finding the middle node:

def find_middle_node(self):
    slow = self.head
    faster = self.head
    while (faster.next != None):
        faster = faster.next
        if (faster.next != None):
            faster = faster.next
        slow = slow.next
    return slow

#Method for finding if the node has loops
    def has_loop(self): #Floyd's cycle finding algorithm or totoise and hare algorithm
        slow=self.head
        faster=self.head
        while(faster.next!=None):
            faster=faster.next
            if(faster.next==None):
                return False
            else:
                faster=faster.next
                if(faster==slow):
                    return True
                slow=slow.next
                if(faster==slow):
                    return True
        return False


#####################################################
#find the kth node from the end

def find_kth_from_end(ll,k):
    slower=ll.head
    faster=ll.head
    for _ in range(k):
        if faster is None:
            return None
        faster=faster.next
    while faster:
        slower=slower.next
        faster=faster.next
    return slower