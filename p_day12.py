#removing duplicates

def remove_duplicates(self):
    if (self.length == 0):
        return None
    temp = self.head
    pre = self.head
    v = []
    while (temp is not None):
        if (temp.value in v):
            pre.next = temp.next
            temp.next = None
            temp = pre.next
            self.length -= 1
        else:
            temp = temp.next
            v.append(temp.value)
        pre = pre.next
###############################
#Double Linked List
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

    def print_list(self):
        temp=self.head
        while(temp is not None):
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
            self.length=1
        else:
            '''temp=self.head
            prea=None
            while(temp.next!=None):
                prea=temp
                temp=temp.next
            temp.next=new_node
            new_node.prev=prea'''
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.length+=1
        return True

    def pop(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            self.head=None
            self.tail=None
            self.length=0
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
            self.length-=1
        return True

dll=DoubleLinkedList(10)
dll.append(20)
dll.append(30)
dll.append(40)
print("Nodes in the double linked list are: ")
dll.print_list()
dll.pop()
print("after pop")
dll.print_list()


