class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def get(self,index):
        if(index>0 or index>=self.length):
            return None
        temp=self.head
        if(index<self.length/2):
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp

    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        if(index<0 or index>self.length):
            return False
        new_node=Node(value)
        if(index==0):
            self.head=new_node
            self.tail=new_node
        elif(index==self.length):
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        else:
            temp = self.get(index - 1)
            tn=temp.next
            temp.next=new_node
            new_node.prev=tn.prev
            new_node.next=tn
            tn.prev=new_node
        self.length+=1
        return True

    def remove(self,index):
        if(index<0 or index>=self.length):
            return None
        if(index==0):
            return self.popfirst(index)
        elif(index==self.length-1):
            return self.pop(index)
        else:
            temp=self.get(index)
            temp.next.prev=temp.prev
            temp.prev.next=temp.next
            temp.next=None
            temp.prev=None
            self.length-=1
            return temp


########
#swap first and last value in DLL
    def swap_first_last(self):
        if (self.length == 0 or self.length == 1):
            return False
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp

    def reverse(self):
        temp=self.head
        if(self.length==0 or self.length==1):
            return False
        while(temp):
            temp.prev,temp.next = temp.next,temp.prev
            temp=temp.prev
        self.head,self.tail = self.tail,self.head


    def is_palindrome(self):
        s=self.head
        e=self.tail
        while(s or e):
            if(s.value!=e.value):
                return False
            s=s.next
            e=e.prev
        return True





